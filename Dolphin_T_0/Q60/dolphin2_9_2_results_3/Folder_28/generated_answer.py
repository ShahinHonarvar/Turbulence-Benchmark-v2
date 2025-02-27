def all_left_right_truncatable_prime(t):
    x = t[19]

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2 or n == 3:
            return True
        elif n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_truncatable(n // 10) and is_truncatable(n % 10) and is_prime(n) and (n % 10 != 0) and (n // 10 % 10 != 0)
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)])