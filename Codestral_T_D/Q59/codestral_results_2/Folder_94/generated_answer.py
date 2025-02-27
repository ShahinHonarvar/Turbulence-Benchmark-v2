def all_left_truncatable_prime(t):
    x = t[43]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_trunc(n):
        while n > 0:
            n //= 10
            if not is_prime(n):
                return False
        return True
    return sorted(filter(left_trunc, range(2, x)))