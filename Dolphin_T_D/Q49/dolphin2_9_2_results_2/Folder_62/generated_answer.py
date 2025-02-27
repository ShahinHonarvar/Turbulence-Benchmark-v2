def if_decimal_is_divisible(binary_rep):
    a, b = (0, 1)
    i = 0
    while i != 130:
        a, b = (b, a + b)
        i += 1
    decimal = int(binary_rep, 2)
    return decimal % b == 0