def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_115 = 1810959246142276611530957
    return decimal_value % fibonacci_115 == 0