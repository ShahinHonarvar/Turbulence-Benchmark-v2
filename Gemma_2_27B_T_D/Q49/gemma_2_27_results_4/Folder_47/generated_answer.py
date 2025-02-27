def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_94 = 197402742198
    return decimal_number % fibonacci_94 == 0