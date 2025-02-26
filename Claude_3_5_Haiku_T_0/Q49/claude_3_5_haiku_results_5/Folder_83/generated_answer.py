def if_decimal_is_divisible(binary_str):

    def fibonacci_60th():
        a, b = (0, 1)
        for _ in range(59):
            a, b = (b, a + b)
        return b
    decimal_num = int(binary_str, 2)
    fib_60 = fibonacci_60th()
    return decimal_num % fib_60 == 0