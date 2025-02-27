def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_144 = 1296667386118400
    return decimal_value % fibonacci_144 == 0