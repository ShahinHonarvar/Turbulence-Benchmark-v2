def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_ninth = 34
    return decimal_integer % fibonacci_ninth == 0