def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(p):
    q = p
    while q != 0:
        if not is_prime(q):
            return False
        q //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[50]
    primes = [i for i in range(x, 0, -1) if is_prime(i)]
    return sorted([i for i in primes if is_right_truncatable(i)], reverse=True)