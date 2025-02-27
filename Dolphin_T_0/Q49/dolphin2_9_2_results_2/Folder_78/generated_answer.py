def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    a, b = (0, 1)
    for _ in range(114):
        a, b = (b, a + b)
    return decimal % b == 0