def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_67 = 1597196046793962
    return decimal_integer % fibonacci_67 == 0