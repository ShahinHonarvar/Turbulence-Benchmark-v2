def all_right_truncatable_prime(x_tup):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_right_truncatable(n // 10)
    x = x_tup[0]
    return sorted([i for i in range(x - 1, 1, -1) if is_right_truncatable(i)], reverse=False)