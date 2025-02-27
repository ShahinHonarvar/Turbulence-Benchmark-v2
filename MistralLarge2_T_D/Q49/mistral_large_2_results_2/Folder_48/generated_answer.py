def if_decimal_is_divisible(binary_rep):

    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(n - 1):
                a, b = (b, a + b)
            return b
    decimal_value = int(binary_rep, 2)
    fib_198th = fib(198)
    return decimal_value % fib_198th == 0