def all_left_truncatable_prime(t):

    def check(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if check(n):
            i = 1
            m = n
            while m > 1:
                m //= 10
                i *= 10
            while n % i != n:
                if not check(n // i):
                    return False
                i //= 10
                n //= 10
        return True
    x = t[86]
    l = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    l.sort()
    return l