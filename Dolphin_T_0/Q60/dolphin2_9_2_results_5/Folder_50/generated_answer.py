def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        return is_prime(n) and is_truncatable(n // 10) and is_truncatable(n % 10)
    x = t[57]
    left_right_truncatable_primes = [n for n in range(x, 0, -1) if is_truncatable(n)]
    return left_right_truncatable_primes