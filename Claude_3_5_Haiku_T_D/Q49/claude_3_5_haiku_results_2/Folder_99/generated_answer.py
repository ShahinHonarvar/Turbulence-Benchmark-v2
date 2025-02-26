def if_decimal_is_divisible(binary_str):

    def fibonacci_109th():
        a, b = (0, 1)
        for _ in range(108):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_109 = fibonacci_109th()
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib_109 == 0