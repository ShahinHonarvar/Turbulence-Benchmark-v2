def if_decimal_is_divisible(binary_str):
    fibonacci_13 = 144
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fibonacci_13 == 0