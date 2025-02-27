def if_decimal_is_divisible(binary_string):
    decimal_representation = int(binary_string, 2)
    return decimal_representation % 8 == 0