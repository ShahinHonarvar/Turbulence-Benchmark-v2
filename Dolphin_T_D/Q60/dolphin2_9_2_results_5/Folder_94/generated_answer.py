def all_left_right_truncatable_prime(in_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_left(n):
        if n < 2:
            return False
        x = n
        while x >= 10:
            x = x % int(x / 10)
            if not is_prime(x):
                return False
        return True

    def is_truncatable_right(n):
        if n < 2:
            return False
        x = n
        while x >= 10:
            x = int(x / 10)
            if not is_prime(x):
                return False
        return True

    def is_truncatable_left_and_right(n):
        return is_truncatable_left(n) and is_truncatable_right(n)
    x = in_tuple[43]
    return sorted([i for i in range(x + 1) if is_prime(i) and is_truncatable_left_and_right(i)])