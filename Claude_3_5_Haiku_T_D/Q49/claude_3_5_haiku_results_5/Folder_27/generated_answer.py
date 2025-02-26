def if_decimal_is_divisible(binary_str):

    def fibonacci_87th_number():
        a, b = (0, 1)
        for _ in range(86):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_number = fibonacci_87th_number()
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib_number == 0