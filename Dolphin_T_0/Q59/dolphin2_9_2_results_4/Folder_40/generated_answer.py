from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[10]
    prime_nums = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for num in prime_nums:
        str_num = str(num)
        while str_num:
            if not isprime(int(str_num)):
                break
            str_num = str_num[1:]
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)