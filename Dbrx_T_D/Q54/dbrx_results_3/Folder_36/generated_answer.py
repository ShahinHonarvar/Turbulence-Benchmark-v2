from sympy import isprime

def all_right_truncatable_prime(args):
    x = args[992]
    primes = [i for i in range(2, x) if isprime(i) and is_right_truncatable_prime(i)]
    return sorted(primes)

def is_right_truncatable_prime(n):
    while n > 9:
        n /= 10
        if not isprime(int(n)):
            return False
    return True