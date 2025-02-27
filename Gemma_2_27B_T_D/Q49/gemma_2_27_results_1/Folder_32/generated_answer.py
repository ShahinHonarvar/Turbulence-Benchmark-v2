def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_178 = 63245986
    return decimal_value % fibonacci_178 == 0