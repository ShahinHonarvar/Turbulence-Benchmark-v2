def all_left_right_truncatable_prime(t):

    def check(n):

        def is_prime(m):
            if m < 2:
                return False
            for i in range(2, int(m ** 0.5) + 1):
                if m % i == 0:
                    return False
            return True
        while n > 0:
            if is_prime(n):
                n //= 10
            else:
                return False
        return True
    x = t[88]
    res = [i for i in range(2, x + 1) if check(i)]
    return res