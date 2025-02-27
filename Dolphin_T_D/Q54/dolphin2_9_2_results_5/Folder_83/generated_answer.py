def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[24]
    l = []
    for i in range(x):
        if is_prime(i):
            r = i
            while r > 0:
                if not is_prime(r):
                    break
                r //= 10
                if r == 0:
                    l.append(i)
    return sorted(l)