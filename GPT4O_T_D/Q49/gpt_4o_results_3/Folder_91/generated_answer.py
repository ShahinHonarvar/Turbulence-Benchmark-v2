def if_decimal_is_divisible(binary_string):
    fibonacci_sixth = 5
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_sixth == 0