def if_decimal_is_divisible(binary_str):

    def fibonacci_24():
        a, b = (0, 1)
        for _ in range(24):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_24() == 0