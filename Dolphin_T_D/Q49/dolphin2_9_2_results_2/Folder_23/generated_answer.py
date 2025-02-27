def if_decimal_is_divisible(binary_rep):
    n = binary_rep.index('1', 0)
    binary_rep = binary_rep[n:]
    x = 0
    y = 1
    i = 0
    while i < 48 - n:
        x, y = (y, x + y)
        i += 1
    return binary_rep % y == 0