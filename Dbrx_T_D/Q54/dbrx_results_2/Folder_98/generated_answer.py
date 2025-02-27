from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[8]
    primes = []
    for i in range(10, x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_right_truncatable_prime(n):
    while n > 1:
        if not isprime(n):
            return False
        n = n // 10
    return True