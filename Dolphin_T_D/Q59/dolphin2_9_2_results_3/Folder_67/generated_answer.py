def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 2:
            return False
        while n:
            if n % 10 == 0:
                return False
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[71]
    return sorted([i for i in range(x - 1, 1, -1) if is_truncatable(i)], reverse=False)