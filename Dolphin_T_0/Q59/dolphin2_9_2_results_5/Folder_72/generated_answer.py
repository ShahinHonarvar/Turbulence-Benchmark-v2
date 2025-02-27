def all_left_truncatable_prime(x):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n in (1, 4) or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        if not is_prime(n):
            return False
        while n > 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    return sorted([i for i in range(2, x) if left_truncatable(i)], reverse=True)