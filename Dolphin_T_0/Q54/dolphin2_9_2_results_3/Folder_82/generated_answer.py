def all_right_truncatable_prime(t):
    x = t[69]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([i for i in range(2, x) if is_right_truncatable(i)], reverse=True)