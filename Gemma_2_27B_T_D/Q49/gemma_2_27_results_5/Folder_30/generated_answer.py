def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_186 = 258415
    return decimal % fibonacci_186 == 0