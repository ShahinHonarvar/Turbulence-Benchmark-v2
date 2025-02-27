def all_left_right_truncatable_prime(t):
    x = t[97]

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
        while n != 0:
            if n % 10 == 0 or not is_prime(n):
                return False
            n = n // 10
        return True

    def is_left_right_truncatable_prime(n):
        while n != 0:
            if n < 10:
                if is_truncatable(n) and is_prime(n):
                    return True
                else:
                    return False
            elif not (is_truncatable(n) and is_left_right_truncatable_prime(n // 10) and is_left_right_truncatable_prime(n % 10)):
                return False
        return False
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)])