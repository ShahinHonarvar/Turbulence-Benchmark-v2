def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    a, b = (0, 1)
    for _ in range(96):
        a, b = (b, a + b)
    return decimal % b == 0