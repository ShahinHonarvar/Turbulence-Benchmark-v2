def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_94 = 190392490709135
    return decimal_number % fibonacci_94 == 0