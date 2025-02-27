def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    while n > 0 and is_prime(n):
        n //= 10
    return n == 0

def all_left_truncatable_prime(t):
    x = t[45]
    return sorted([i for i in range(2, x) if truncate_left(i)], reverse=True)