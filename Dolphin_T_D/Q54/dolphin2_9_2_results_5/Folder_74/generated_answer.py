def all_right_truncatable_prime(t):

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

    def right_truncatable_prime(n):
        s = str(n)
        n = len(s)
        if n == 1:
            return is_prime(n)
        else:
            return is_prime(n) and right_truncatable_prime(int(s[:-1]))
    x = t[36]
    a = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            a.append(i)
    return sorted(a)