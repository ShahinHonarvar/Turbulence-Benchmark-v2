def all_left_truncatable_prime(t):
    x = t[36]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n == 0:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([i for i in range(x - 1, 1, -1) if is_left_truncatable(i) and is_prime(i)], reverse=True)