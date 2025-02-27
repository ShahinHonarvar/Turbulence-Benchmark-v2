def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n // 10 == 0:
            return is_prime(n)
        if not is_prime(n):
            return False
        if n % 10 == 0:
            return False
        return is_truncatable_prime(n // 10) and is_truncatable_prime(n % 10)
    x = t[50]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)