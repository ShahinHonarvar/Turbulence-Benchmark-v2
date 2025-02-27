def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_right_truncatable_prime(n):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[23]
    primes = sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
    return primes if primes else []