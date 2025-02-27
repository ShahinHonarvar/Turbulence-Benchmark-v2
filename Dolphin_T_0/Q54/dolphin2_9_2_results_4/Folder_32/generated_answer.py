def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_rtp(n):
        if not is_prime(n):
            return False
        m = n
        while m > 0:
            m //= 10
            if not is_prime(m):
                return False
        return True
    x = t[42]
    rtps = [i for i in range(x) if is_rtp(i)]
    return sorted(rtps, key=int)