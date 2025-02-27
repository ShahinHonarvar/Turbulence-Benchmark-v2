def if_decimal_is_divisible(binary_rep):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    return int(binary_rep, 2) % fib(199) == 0