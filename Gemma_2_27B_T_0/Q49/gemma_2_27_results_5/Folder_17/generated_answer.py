def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_154 = 927372692193078999173
    return decimal_number % fibonacci_154 == 0