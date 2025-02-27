def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = round(n ** 0.5)
        for d in range(3, 1 + max_div, 2):
            if n % d == 0:
                return False
        return True

    def left_right_truncatable_prime(n):
        n_str = str(n)
        while len(n_str) > 1:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[1:-1]
        return True
    x = x_tuple[992]
    return sorted([n for n in range(2, 1 + x) if left_right_truncatable_prime(n)])