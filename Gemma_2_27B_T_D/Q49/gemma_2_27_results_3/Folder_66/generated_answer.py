def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_120 = 3467742179871
    return decimal % fibonacci_120 == 0