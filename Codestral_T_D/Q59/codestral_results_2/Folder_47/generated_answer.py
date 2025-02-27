def all_left_truncatable_prime(t):
    x = t[49]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n = truncate_left(n)
            if not is_prime(n):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])