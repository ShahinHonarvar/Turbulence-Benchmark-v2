def all_left_right_truncatable_prime(y):

    def is_prime(n):
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        return all((int(str(n).slice(i, -i)) % 2 != 0 and is_prime(int(str(n).slice(i, -i))) for i in range(1, len(str(n)) - 1)))
    x = y[86]
    return sorted([i for i in range(2, x + 1) if left_right_truncatable(i)], lru_cache=is_prime)