def if_decimal_is_divisible(binary_string):

    def fibonacci_95():
        a, b = (0, 1)
        for _ in range(94):
            a, b = (b, a + b)
        return b
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_95() == 0