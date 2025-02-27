def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    n = 187
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return decimal_value % b == 0