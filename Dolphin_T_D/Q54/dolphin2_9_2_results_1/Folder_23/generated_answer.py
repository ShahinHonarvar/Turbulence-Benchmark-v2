def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n == 0:
            return 0
        if is_prime(n):
            return is_truncatable(n // 10)
        return 0
    x = t[77]
    return sorted([n for n in range(x, 0, -1) if is_truncatable(n)], reverse=True)