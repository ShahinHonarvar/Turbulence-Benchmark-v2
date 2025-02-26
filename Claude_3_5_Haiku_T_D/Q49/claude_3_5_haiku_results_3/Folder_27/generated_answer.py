def if_decimal_is_divisible(binary_str):

    def fibonacci_87th():
        a, b = (0, 1)
        for _ in range(86):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_87 = fibonacci_87th()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_87 == 0