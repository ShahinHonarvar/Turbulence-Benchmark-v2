def if_decimal_is_divisible(binary_rep):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_rep, 2)
    fib_108 = fib(108)
    return decimal_value % fib_108 == 0