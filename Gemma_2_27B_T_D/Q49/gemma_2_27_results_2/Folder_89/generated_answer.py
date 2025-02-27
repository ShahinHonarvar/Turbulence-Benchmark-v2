def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_126 = 127755800749810207849669795539648727739462854840027
    return decimal_value % fibonacci_126 == 0