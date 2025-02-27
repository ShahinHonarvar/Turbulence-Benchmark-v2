def all_left_right_truncatable_prime(t):

    def check(n, t):
        if n <= 1 or '0' in str(n):
            return False
        for x in t:
            n = int(str(n).replace(x, ''))
        return n != 1

    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    l = []
    x = t[6]
    for n in range(11, x + 1):
        if check_prime(n):
            if check(n, str(n)):
                l.append(n)
    return sorted(l, reverse=True)