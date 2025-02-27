def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_160 = 165580141
    return decimal_integer % fibonacci_160 == 0