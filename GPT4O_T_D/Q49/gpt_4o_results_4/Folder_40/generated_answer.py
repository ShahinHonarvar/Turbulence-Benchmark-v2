def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    return decimal_num % 3 == 0