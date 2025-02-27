def if_decimal_is_divisible(binary):
    a, b, c, d = (int(binary[0]), int(binary[1]), 0, 0)
    for i in range(2, len(binary)):
        d = (a + b + c) % 27 + d
        a, b, c = (b, c, d)
    return d % 27 == 0