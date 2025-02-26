def if_decimal_is_divisible(binary_str):

    def fibonacci_104():
        a, b = (0, 1)
        for _ in range(103):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_104 = fibonacci_104()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_104 == 0