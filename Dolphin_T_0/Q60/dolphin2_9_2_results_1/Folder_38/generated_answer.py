def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_left_right_truncatable_prime(int(n / 10))
        return False
    x = t[28]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])