def if_decimal_is_divisible(binary_str):

    def fib_80():
        a, b = (0, 1)
        for _ in range(79):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    divisor = fib_80()
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % divisor == 0