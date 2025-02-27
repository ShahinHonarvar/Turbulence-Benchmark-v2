def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_24 = 46368
    return decimal_value % fibonacci_24 == 0