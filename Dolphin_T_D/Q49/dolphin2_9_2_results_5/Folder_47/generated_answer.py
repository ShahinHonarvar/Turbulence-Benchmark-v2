def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    i = 0
    x, y = (0, 1)
    while i < 94:
        x, y = (y, x + y)
        i += 1
    return decimal % y == 0