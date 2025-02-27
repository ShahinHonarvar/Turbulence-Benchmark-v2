def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_74 = 1304977471735
    return decimal_number % fibonacci_74 == 0