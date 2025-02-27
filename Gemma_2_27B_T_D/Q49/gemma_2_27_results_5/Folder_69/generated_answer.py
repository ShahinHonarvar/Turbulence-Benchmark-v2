def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_170 = 129717127213010043
    return decimal_value % fibonacci_170 == 0