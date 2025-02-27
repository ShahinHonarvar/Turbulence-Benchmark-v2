def all_left_right_truncatable_prime(t):
    x = t[38]

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

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_left(n)
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_right(n)
        return True
    left_right_truncatable_primes = [n for n in range(2, x + 1) if '0' not in str(n) and is_prime(n) and is_left_truncatable(n) and is_right_truncatable(n)]
    return sorted(left_right_truncatable_primes, reverse=True)