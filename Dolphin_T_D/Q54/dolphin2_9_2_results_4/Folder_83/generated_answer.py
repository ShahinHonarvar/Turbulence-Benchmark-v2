def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 1:
            n = int(n / 10)
            if not is_prime(n):
                return False
        return True
    x = t[24]
    result = [n for n in range(2, x) if is_right_truncatable(n) and is_prime(n)]
    return sorted(result)