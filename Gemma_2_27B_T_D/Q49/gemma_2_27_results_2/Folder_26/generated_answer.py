def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_138 = 299576
    return decimal_integer % fibonacci_138 == 0