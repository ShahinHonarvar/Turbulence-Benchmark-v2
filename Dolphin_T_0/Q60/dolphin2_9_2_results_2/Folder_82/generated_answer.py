def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 5 or n % 5 == 0:
            return False
        while n > 10:
            if n % 10 == 0:
                return False
            if not is_prime(int(n // 10) % 10 * 10 + n % 10):
                return False
            n //= 10
        return True
    x = t[69]
    return sorted([n for n in range(x, 0, -1) if is_left_right_truncatable_prime(n)])