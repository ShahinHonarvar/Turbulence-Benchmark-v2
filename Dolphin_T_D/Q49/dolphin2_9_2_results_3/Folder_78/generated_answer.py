def if_decimal_is_divisible(binary_rep):
    a, b = (0, 1)
    for _ in range(114):
        a, b = (b, a + b)
    decimal = int(binary_rep, 2)
    return decimal % b == 0