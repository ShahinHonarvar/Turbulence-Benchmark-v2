def all_left_right_truncatable_prime(t):
    x = t[97]

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

    def is_left_truncatable(n):
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        while n >= 10:
            n = n // 10
            if not is_prime(n):
                return False
        return True

    def is_left_right_truncatable(n):
        return is_left_truncatable(n) and is_right_truncatable(n)
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n)], reverse=True)