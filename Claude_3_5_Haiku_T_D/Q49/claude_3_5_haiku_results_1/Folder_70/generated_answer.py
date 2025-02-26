def if_decimal_is_divisible(binary_string):

    def fibonacci_137():
        a, b = (0, 1)
        for _ in range(136):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_137 = fibonacci_137()
    decimal_num = binary_to_decimal(binary_string)
    return decimal_num % fib_137 == 0