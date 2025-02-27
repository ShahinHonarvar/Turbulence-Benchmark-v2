def is_prime(n):
    if n == 1:
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

def right_truncatable_prime(n):
    m = n
    while m != 0:
        if not is_prime(m):
            return False
        m = m // 10
    return True

def all_right_truncatable_prime(t):
    x = t[70]
    primes = []
    for i in range(x):
        if is_prime(i) and right_truncatable_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes if primes else []