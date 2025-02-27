def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    x = t[945]
    return sorted([i for i in range(2, x + 1) if is_left_truncatable_prime(i) and is_right_truncatable_prime(i)], reverse=True)