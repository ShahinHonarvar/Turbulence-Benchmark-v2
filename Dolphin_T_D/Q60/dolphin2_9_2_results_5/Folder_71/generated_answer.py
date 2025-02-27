def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        while n > 10:
            if not is_prime(n // 10) or not is_prime(int(n % 10)):
                return False
            n //= 10
            n %= 10
        return is_prime(n)
    x = t[22]
    l = []
    for i in range(x, 1, -1):
        if is_prime(i) and left_right_truncatable(i):
            l.append(i)
    return l