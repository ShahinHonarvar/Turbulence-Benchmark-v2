def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_146 = 1355440646297970857
    return decimal_number % fibonacci_146 == 0