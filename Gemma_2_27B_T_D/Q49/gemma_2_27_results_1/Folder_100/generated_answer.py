def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_190 = 956722026041
    return decimal_value % fibonacci_190 == 0