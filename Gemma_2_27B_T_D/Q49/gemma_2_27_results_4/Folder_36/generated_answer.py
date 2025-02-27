def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_150 = 99621409987
    return decimal_value % fibonacci_150 == 0