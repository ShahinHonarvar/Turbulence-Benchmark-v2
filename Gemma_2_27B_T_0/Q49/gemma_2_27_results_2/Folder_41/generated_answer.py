def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_67 = 1500549019349
    return decimal_number % fibonacci_67 == 0