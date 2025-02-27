def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(p):
    p = str(p)
    for i in range(1, len(p)):
        if not is_prime(int(p[:-i])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[54]
    primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(primes) if primes else []