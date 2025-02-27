import sympy

def is_truncatable_prime(n):
    n = str(n)
    while len(n) > 1:
        if n[1] == '0':
            return False
        n = n[1:-1]
        if not sympy.isprime(int(n)):
            return False
    return sympy.isprime(int(n))

def all_left_right_truncatable_prime(x):
    primes = list(sympy.primerange(2, x + 1))
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)