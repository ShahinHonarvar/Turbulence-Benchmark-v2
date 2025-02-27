def all_left_right_truncatable_prime(tup):
    x = tup[98]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        while len(str(n)) > 1:
            n = truncate_left(n)
            if not is_prime(n):
                return False
            if len(str(n)) > 1:
                n = truncate_right(n)
                if not is_prime(n):
                    return False
        return True
    return sorted((n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)))