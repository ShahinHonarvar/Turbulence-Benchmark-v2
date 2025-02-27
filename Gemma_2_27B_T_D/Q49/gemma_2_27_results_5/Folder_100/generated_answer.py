def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_190 = 10119943992389948376
    return decimal_value % fibonacci_190 == 0