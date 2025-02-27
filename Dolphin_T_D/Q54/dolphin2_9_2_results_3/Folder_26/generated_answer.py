import sympy

def is_right_truncatable_prime(n):
    while n > 0:
        if not sympy.isprime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(tu):
    x = tu[81]
    primes = []
    for i in range(2, x):
        if sympy.isprime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)