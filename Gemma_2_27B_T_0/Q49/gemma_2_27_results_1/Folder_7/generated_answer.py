def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_160 = 102334155
    return decimal_number % fibonacci_160 == 0