def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_114 = 1134903170
    return decimal_value % fibonacci_114 == 0