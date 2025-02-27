def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_144 = 106569844109
    return decimal_value % fibonacci_144 == 0