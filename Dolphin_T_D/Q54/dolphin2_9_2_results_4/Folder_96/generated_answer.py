def all_right_truncatable_prime(t):
    x = t[29]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        return is_prime(n) and is_right_truncatable_prime(n // 10)
    return sorted([n for n in range(3, x) if is_right_truncatable_prime(n)])