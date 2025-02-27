def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    x = t[6]
    res = []
    for n in range(x, 1, -1):
        if is_prime(n) and all((is_prime(n // 10 ** i) for i in range(1, len(str(n))))) and (n % 5 != 0) and (n != 1):
            res.append(n)
    return res