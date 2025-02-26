def if_decimal_is_divisible(binary_str):

    def fibonacci_99():
        a, b = (0, 1)
        for _ in range(98):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_99 = fibonacci_99()
    decimal = binary_to_decimal(binary_str)
    return decimal % fib_99 == 0