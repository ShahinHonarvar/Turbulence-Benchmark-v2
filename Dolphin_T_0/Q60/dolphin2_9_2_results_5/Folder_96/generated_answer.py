def all_left_right_truncatable_prime(t):
    x = t[29]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 9:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return is_prime(n)
    return [n for n in range(2, x + 1) if is_truncatable(n)]