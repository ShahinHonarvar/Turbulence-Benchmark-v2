def is_right_truncatable_prime(n, x):
    while n < x:
        if not all((int(n) % d for d in range(2, int(n ** 0.5) + 1))):
            return False
        n //= 10
    return all((int(n) % d for d in range(2, int(n ** 0.5) + 1)))

def all_right_truncatable_prime(t):
    x = t[38]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i, x)], reverse=True)