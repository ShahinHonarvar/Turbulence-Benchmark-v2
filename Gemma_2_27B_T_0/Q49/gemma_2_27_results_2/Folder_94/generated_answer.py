def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_40 = 102334155
    return decimal_number % fibonacci_40 == 0