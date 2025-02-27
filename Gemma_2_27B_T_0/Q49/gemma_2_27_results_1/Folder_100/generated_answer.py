def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_190 = 1062508070407180800
    return decimal_number % fibonacci_190 == 0