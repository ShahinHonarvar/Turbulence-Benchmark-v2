def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_199 = 966929019467281
    return decimal_integer % fibonacci_199 == 0