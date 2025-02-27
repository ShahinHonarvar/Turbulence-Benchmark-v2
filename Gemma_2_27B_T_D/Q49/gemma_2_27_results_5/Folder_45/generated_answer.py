def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_28 = 317811
    return decimal_value % fibonacci_28 == 0