from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[80]
    prime_list = [i for i in range(2, x + 1) if isprime(i)]
    left_right_truncatable_prime_list = []
    for prime in prime_list:
        str_prime = str(prime)
        if any((digit == '0' for digit in str_prime)):
            continue
        while len(str_prime) > 1:
            str_prime = str_prime[1:-1]
            if not isprime(int(str_prime)):
                break
        else:
            left_right_truncatable_prime_list.append(prime)
    left_right_truncatable_prime_list.sort(reverse=True)
    return left_right_truncatable_prime_list