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

def right_truncatable(n):
    num = n
    while num != 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[28]
    primes = []
    for i in range(2, x):
        if right_truncatable(i):
            primes.append(i)
    primes.sort()
    return primes