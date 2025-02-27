def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_144 = 12880252076844012875
    return decimal_number % fibonacci_144 == 0