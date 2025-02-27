from sympy import prime_to_int

def is_left_truncatable(n):
    while n:
        if not sympy.isprime(n):
            return False
        n = n // 10
    return True

def all_left_truncatable_prime(t):
    x = t[433]
    primes = [i for i in range(2, x) if sympy.isprime(i)]
    left_truncatable_primes = [i for i in primes if is_left_truncatable(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes