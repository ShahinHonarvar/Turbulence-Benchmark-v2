def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_35 = 9227465
    return decimal_value % fibonacci_35 == 0