def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    a, b = (0, 1)
    for i in range(158):
        a, b = (b, a + b)
    return decimal_value % b == 0