def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            n = int(n) // 10
            if n > 0 and (not is_prime(n)):
                return False
        return True
    x = 10 ** 67
    for i in range(t[0], x):
        if is_prime(i) and is_right_truncatable(i):
            yield i
    for i in range(t[1], x):
        if is_prime(i) and is_right_truncatable(i):
            yield i