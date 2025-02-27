def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_95 = 23416728348467685
    return decimal_number % fibonacci_95 == 0