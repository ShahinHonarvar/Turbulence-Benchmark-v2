def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_154 = 578721299661181
    return decimal_value % fibonacci_154 == 0