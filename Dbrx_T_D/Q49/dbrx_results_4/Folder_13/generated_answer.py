def if_decimal_is_divisible(bin_repr):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n):
                a, b = (b, a + b)
            return b
    decimal = int(bin_repr, 2)
    fib_num = fibonacci(174)
    return decimal % fib_num == 0