def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    return decimal_num % 3 == 0