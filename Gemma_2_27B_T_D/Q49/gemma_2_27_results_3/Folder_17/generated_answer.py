def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_154 = 927372692193078999173
    return decimal_integer % fibonacci_154 == 0