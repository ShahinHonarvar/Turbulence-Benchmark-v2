def if_decimal_is_divisible(binary_string):

    def fibonacci_40th():
        a, b = (0, 1)
        for _ in range(39):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_40 = fibonacci_40th()
    decimal_value = binary_to_decimal(binary_string)
    return decimal_value % fib_40 == 0