def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_126 = 12586269025
    return decimal_number % fibonacci_126 == 0