def if_decimal_is_divisible(binary_rep):
    num = int(binary_rep, 2)
    i = 84
    a, b = (0, 1)
    while i > 0:
        a, b = (b, a + b)
        i -= 1
    return num % b == 0