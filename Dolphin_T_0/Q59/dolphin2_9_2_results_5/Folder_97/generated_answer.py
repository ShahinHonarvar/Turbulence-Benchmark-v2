def all_left_truncatable_prime(t):

    def is_prime(y):
        if y % 2 == 0 and y > 2:
            return False
        for i in range(3, int(y ** 0.5) + 1, 2):
            if y % i == 0:
                return False
        return True

    def is_left_truncatable_prime(y):
        if y < 2 or '0' in str(y):
            return False
        while y != 0:
            if not is_prime(y):
                return False
            y = y // 10
        return True
    x = t[645]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])