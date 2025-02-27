def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a = 0
    b = 1
    for i in range(2, 80):
        c = a + b
        a = b
        b = c
    return decimal_representation % b == 0