def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_179 = 4181
    return decimal_value % fibonacci_179 == 0