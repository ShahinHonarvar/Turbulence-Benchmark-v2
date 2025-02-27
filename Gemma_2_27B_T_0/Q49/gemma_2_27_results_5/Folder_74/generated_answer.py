def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_166 = 109461728348612466819
    return decimal_number % fibonacci_166 == 0