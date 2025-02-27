def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_170 = 104498612417127
    return decimal_value % fibonacci_170 == 0