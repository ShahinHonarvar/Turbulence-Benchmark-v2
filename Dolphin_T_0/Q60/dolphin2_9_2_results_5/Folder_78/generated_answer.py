from sympy import isprime

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[2]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if isprime(num) and (not '0' in str(num)):
            for i in range(len(str(num)))[::-1]:
                if not isprime(int(str(num)[i:])):
                    break
            else:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)