def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_135 = 281408606820993
    return decimal_value % fibonacci_135 == 0