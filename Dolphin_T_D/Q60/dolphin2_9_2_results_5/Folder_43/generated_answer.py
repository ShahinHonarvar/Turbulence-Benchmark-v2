def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def check_truncatable(x):
        while x:
            if not is_prime(int(x)):
                return False
            x = x[1:-1]
        return True
    x = t[89]
    res = []
    for i in range(2, x + 1):
        if is_prime(i):
            if check_truncatable(str(i)):
                res.append(i)
    return sorted(res, reverse=True)