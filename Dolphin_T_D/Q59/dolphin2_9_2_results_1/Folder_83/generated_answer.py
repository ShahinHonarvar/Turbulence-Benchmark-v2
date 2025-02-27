def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2 or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            return False
        return True

    def is_left_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[24]
    return sorted([i for i in range(2, x) if is_left_truncatable(i)])