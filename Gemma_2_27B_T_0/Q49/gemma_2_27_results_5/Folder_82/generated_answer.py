def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_99 = 218922995834555169026
    return decimal_value % fibonacci_99 == 0