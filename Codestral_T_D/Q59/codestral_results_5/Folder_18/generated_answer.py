def all_left_truncatable_prime(t):
    x = t[429]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)