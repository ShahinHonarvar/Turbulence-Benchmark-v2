def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while n:
            if n < 2:
                return False
            p = n
            while p % 10 > 1:
                p //= 10
                if not is_prime(p):
                    return False
            n //= 10
        return True
    x = t[370]
    return sorted([i for i in range(x - 1, 0, -1) if is_truncatable_prime(i)])