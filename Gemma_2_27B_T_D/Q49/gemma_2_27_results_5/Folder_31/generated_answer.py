def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_69 = 1162261467
    return decimal_value % fibonacci_69 == 0