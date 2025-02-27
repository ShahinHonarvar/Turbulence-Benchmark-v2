def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_104 = 10627717792
    return decimal_number % fibonacci_104 == 0