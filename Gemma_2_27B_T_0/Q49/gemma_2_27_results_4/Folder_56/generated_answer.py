def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_84 = 180999700776487
    return decimal_number % fibonacci_84 == 0