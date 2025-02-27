def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_146 = 409201968160
    return decimal_value % fibonacci_146 == 0