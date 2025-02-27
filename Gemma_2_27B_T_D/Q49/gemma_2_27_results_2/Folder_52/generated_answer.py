def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_176 = 258479791916583
    return decimal_value % fibonacci_176 == 0