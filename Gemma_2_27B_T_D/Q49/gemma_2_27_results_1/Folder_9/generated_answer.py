def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_68 = 2189251670
    return decimal_value % fibonacci_68 == 0