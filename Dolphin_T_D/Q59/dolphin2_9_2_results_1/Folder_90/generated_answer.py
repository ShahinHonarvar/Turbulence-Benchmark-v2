def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if '0' in str(n) or not is_prime(n):
            return False
        i = 1
        while True:
            m = int(str(n)[i:])
            if not is_prime(m):
                return False
            if m < 10:
                break
            i += 1
        return True
    x = t[466]
    res = []
    for i in range(x, 1, -1):
        if is_truncatable_prime(i):
            res.append(i)
    return res