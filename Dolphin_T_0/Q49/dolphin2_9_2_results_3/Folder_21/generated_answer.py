def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    a, b = (0, 1)
    for _ in range(194):
        a, b = (b, a + b)
    return dec % b == 0