def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_divisor = 2
    return decimal_number % fibonacci_divisor == 0