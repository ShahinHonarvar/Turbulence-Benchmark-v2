def all_left_truncatable_prime(t):
    x = t[64]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 2 or str(n).count('0') > 0:
            return False
        m = n
        while m > 1:
            if not is_prime(m):
                return False
            m //= 10
        return True
    res = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(res, reverse=True)