def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_196 = 10627008998976000
    return decimal_number % fibonacci_196 == 0