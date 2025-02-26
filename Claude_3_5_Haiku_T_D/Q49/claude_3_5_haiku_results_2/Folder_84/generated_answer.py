def if_decimal_is_divisible(binary_str):

    def fibonacci_196():
        a, b = (0, 1)
        for _ in range(195):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_196 = fibonacci_196()
    decimal_number = binary_to_decimal(binary_str)
    return decimal_number % fib_196 == 0