def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return True
        if n % 10 == 0:
            return False
        return is_right_truncatable(n // 10) and is_prime(n)
    l = []
    x = t[23]
    if x > 1:
        for i in range(2, x):
            if is_right_truncatable(i):
                l.append(i)
    return sorted(l)