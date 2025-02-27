def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_string, 2)
    fib_199 = fibonacci(199)
    return decimal_value % fib_199 == 0