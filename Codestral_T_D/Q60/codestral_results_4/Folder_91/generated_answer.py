def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_left_right_truncatable_prime(n):
        if n < 2 or '0' in str(n):
            return False
        while n >= 10:
            n = truncate_left(n)
            if not is_prime(n):
                return False
        n = tup[0]
        while n >= 10:
            n = truncate_right(n)
            if not is_prime(n):
                return False
        return True
    return sorted([n for n in range(2, tup[0] + 1) if is_left_right_truncatable_prime(n)], reverse=True)