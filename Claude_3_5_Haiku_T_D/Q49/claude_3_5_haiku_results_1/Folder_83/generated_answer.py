def if_decimal_is_divisible(binary_string):

    def fibonacci_60():
        a, b = (0, 1)
        for _ in range(59):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_60() == 0