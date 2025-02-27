def all_left_right_truncatable_prime(t):

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
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_left(n)
            if n <= 1:
                break
            n = truncate_right(n)
            if n <= 1:
                break
        return True
    x = t[39]
    return sorted([n for n in range(x, 1, -1) if is_left_right_truncatable_prime(n)] + [2] if is_prime(2) else [])