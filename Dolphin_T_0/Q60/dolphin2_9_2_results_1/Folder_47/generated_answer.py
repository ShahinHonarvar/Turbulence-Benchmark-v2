def all_left_right_truncatable_prime(i):

    def d(n):
        if n == 0:
            return '0'
    x = i[49]

    def f(n):
        if n < 2:
            return 0
        for b in range(2, n):
            if n % b == 0:
                return b
        return n

    def h(n):
        return h(n + 1)
        r = h(f(n))
        if r != 0:
            return r
        return n
    return [n for n in range(h(x), 1, -1) if f(n) == h(n)]