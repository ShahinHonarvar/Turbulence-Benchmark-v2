def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_15th = 610
    return decimal_value % fibonacci_15th == 0