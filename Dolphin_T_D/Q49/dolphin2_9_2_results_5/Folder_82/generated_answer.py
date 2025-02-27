def if_decimal_is_divisible(binary_rep):
    n = int(binary_rep, 2)
    i = 0
    a, b = (0, 1)
    while i < 99:
        a, b = (b, a + b)
        i += 1
    return n % b == 0