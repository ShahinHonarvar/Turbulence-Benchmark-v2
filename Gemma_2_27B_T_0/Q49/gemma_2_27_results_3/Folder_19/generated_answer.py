def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_29 = 514229
    return decimal_number % fibonacci_29 == 0