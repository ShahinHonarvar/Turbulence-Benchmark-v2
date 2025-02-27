def is_left_truncatable_prime(n):
    while n > 1:
        if n % 10 == 0:
            return False
        if not all((n % i for i in range(2, int(n ** 0.5) + 1))):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(t):
    x = t[96]
    return sorted([i for i in range(x - 1, 0, -1) if is_left_truncatable_prime(i)])