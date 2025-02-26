def if_decimal_is_divisible(binary_str):

    def fibonacci_95th():
        a, b = (0, 1)
        for _ in range(94):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    divisor = fibonacci_95th()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % divisor == 0