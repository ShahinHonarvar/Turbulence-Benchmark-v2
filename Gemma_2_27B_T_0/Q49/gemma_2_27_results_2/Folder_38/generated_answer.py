def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_78 = 12986269025
    return decimal_number % fibonacci_78 == 0