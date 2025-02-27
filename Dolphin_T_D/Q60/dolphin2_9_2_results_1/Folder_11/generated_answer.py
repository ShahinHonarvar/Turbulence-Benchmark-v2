def all_left_right_truncatable_prime(t):

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
        while n > 9:
            if not is_prime(n // 10) or not is_prime(n % 10):
                return False
            n //= 10
        return True
    j = t[86]
    r = []
    for i in range(2, j + 1):
        if is_truncatable_prime(i):
            r.append(i)
    r.sort()
    return r