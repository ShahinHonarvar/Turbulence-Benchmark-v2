def all_left_right_truncatable_prime(t):
    x = t[14]

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
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_left(n)
            if n < 10:
                break
        n = t[14]
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_right(n)
            if n < 10:
                break
        return True
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)], reverse=True)