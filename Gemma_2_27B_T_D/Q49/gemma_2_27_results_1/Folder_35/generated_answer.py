def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_187 = 16202552748529539207688044213757810
    return decimal_number % fibonacci_187 == 0