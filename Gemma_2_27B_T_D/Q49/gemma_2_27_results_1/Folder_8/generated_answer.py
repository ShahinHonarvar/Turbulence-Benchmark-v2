def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = 102334155
    return decimal_integer % fibonacci_number == 0