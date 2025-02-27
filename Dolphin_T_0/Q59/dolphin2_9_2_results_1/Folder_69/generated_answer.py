def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n == 0:
            return False
        while n > 0:
            if is_prime(n):
                n //= 10
            else:
                return False
        return True
    x = t[760]
    r = []
    for i in range(x, 0, -1):
        if is_prime(i) and is_truncatable(i):
            r.append(i)
    return r