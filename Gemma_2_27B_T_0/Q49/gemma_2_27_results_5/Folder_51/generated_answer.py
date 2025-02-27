def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_17 = 1597
    return decimal_number % fibonacci_17 == 0