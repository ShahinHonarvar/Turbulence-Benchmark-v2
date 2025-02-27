def if_decimal_is_divisible(binary):
    n = 0
    a, b = (0, 1)
    while a < int(binary, 2):
        a, b = (b, a + b)
        n += 1
    return a == 0