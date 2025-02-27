def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    a, b = (0, 1)
    for i in range(119):
        a, b = (b, a + b)
    if decimal % a == 0:
        return True
    else:
        return False