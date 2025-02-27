def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_137 = 139424397926
    return decimal_value % fibonacci_137 == 0