import sympy

def is_truncatable_prime(n):
    while n != 0:
        if not sympy.isprime(n):
            return False
        n = int(n / 10)
    return True

def all_left_truncatable_prime(t):
    x = t[28]
    primes = list(sympy.primerange(2, x))
    truncatable_primes = []
    for p in primes:
        if sympy.isprime(p) and is_truncatable_prime(p):
            truncatable_primes.append(p)
    return sorted(truncatable_primes)