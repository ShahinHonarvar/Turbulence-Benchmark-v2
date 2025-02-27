def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_107 = 3571154466967313
    return decimal_value % fibonacci_107 == 0