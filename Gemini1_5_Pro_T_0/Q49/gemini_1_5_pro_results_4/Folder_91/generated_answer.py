def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    return decimal_representation % 8 == 0