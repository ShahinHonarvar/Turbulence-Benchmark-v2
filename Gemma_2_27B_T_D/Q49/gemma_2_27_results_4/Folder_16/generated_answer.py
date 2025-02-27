def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_128 = 12030947345366
    return decimal_value % fibonacci_128 == 0