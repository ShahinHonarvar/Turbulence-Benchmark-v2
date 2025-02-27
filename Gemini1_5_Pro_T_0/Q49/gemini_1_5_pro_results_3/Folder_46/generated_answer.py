def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a = 0
    b = 1
    for i in range(139):
        a, b = (b, a + b)
    return decimal_representation % a == 0