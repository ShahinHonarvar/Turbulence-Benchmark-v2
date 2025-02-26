def if_decimal_is_divisible(binary_str):

    def fibonacci_60th():
        a, b = (0, 1)
        for _ in range(59):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_60 = fibonacci_60th()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_60 == 0