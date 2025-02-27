def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_105 = 35714572874489856000
    return decimal_number % fibonacci_105 == 0