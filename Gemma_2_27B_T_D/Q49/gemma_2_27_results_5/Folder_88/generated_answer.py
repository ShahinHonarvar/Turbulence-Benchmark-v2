def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_49th = 7778742049
    return decimal_number % fibonacci_49th == 0