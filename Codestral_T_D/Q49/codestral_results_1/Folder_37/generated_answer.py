def if_decimal_is_divisible(bin_str):

    def fibo(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    return int(bin_str, 2) % fibo(46) == 0