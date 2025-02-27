def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_135 = 1299709
    return decimal_number % fibonacci_135 == 0