def if_decimal_is_divisible(binary_string):

    def fibonacci_60th():
        a, b = (0, 1)
        for _ in range(59):
            a, b = (b, a + b)
        return b
    decimal = int(binary_string, 2)
    fib_60 = fibonacci_60th()
    return decimal % fib_60 == 0