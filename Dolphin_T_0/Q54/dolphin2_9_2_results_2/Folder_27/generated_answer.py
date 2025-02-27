def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    l = []
    for n in range(10, x):
        if is_prime(n):
            m = n
            flag = True
            while m > 10 and flag:
                if not is_prime(m // 10):
                    flag = False
                m //= 10
            if flag:
                l.append(n)
    return sorted(l, reverse=True)