def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_115 = 1008094990975872205
    return decimal_value % fibonacci_115 == 0