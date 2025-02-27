def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_137 = 24894756396999322297
    return decimal_integer % fibonacci_137 == 0