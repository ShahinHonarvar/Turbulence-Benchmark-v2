def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_49 = 7778742049
    return decimal_value % fibonacci_49 == 0