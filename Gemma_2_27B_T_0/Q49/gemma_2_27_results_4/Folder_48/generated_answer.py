def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_198 = 1073741824
    return decimal_number % fibonacci_198 == 0