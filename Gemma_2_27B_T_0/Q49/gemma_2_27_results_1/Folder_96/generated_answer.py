def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_47 = 2971215073
    return decimal_value % fibonacci_47 == 0