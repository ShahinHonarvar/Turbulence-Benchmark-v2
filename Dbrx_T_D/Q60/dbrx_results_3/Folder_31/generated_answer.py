from sympy import isprime

def all_left_right_truncatable_prime(n):
    primes = [i for i in range(2, n + 1) if isprime(i)]
    truncatable_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    return truncatable_primes[::-1]

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 10:
        num = int(str(num)[1:])
        if not isprime(num):
            return False
        num = int(str(num)[:-1])
        if not isprime(num) and num != 0:
            return False
    return True