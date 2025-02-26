def if_decimal_is_divisible(binary_str):

    def fibonacci_130th():
        a, b = (0, 1)
        for _ in range(129):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_130 = fibonacci_130th()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_130 == 0