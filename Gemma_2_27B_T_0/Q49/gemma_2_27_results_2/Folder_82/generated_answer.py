def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_99 = 218922995834555169026
    return decimal_number % fibonacci_99 == 0