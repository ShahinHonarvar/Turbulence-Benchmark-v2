def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n ** 0.5 + 1):
        if n % i == 0:
            return False
    return True

def is_rtp(n, base=10):
    if is_prime(n):
        while n:
            if not is_prime(n):
                break
            n //= base
            if n == 0:
                return True
    return False

def all_right_truncatable_prime(t: tuple):
    x = t[31]
    return sorted([i for i in range(2, x) if is_rtp(i)], reverse=True)