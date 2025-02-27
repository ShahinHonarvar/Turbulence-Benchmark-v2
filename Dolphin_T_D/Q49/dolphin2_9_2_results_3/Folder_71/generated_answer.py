def if_decimal_is_divisible(binary_representation):
    decimal_int = int(binary_representation, 2)
    a, b = (0, 1)
    for _ in range(147):
        a, b = (b, a + b)
    return decimal_int % a == 0