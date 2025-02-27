def all_left_truncatable_prime(t):

    def is_left_truncatable_prime(n):
        if n == 0:
            return False
        if not is_prime(n):
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[466]
    return sorted([n for n in range(x) if is_left_truncatable_prime(n)], reverse=True)