def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n == 0 or n // 10 == 0:
            return False
        return is_prime(n) and is_truncatable_prime(n // 10) and is_prime(n % 10)
    x = t[32]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)])