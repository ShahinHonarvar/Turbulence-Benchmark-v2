def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 1:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = t[64]
    lst = [n for i in range(1, x) for n in range(1, i + 1) if is_truncatable_prime(n)]
    return sorted(lst, reverse=True)