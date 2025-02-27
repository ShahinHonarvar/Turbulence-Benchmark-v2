def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while len(str(n)) > 1:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True
    x = t[86]
    ret = [n for n in range(x) if is_prime(n) and is_truncatable_prime(n)]
    return sorted(ret) if ret else []