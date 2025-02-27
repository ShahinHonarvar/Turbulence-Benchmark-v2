def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_29th = 514229
    return decimal_integer % fibonacci_29th == 0