def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    a = 0
    b = 1
    for i in range(45):
        c = a + b
        a = b
        b = c
    if decimal_integer % b == 0:
        return True
    else:
        return False