def if_decimal_is_divisible(binary_representation_string):
    decimal_representation = int(binary_representation_string, 2)
    return decimal_representation % 8 == 0