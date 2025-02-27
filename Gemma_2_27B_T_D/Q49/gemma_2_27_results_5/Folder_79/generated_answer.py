def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_13th = 233
    return decimal_integer % fibonacci_13th == 0