def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_164 = 1060949185451137287
    return decimal_value % fibonacci_164 == 0