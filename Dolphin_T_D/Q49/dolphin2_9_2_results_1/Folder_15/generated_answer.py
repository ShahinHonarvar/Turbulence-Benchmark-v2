def if_decimal_is_divisible(binary_string):
    dec = int(binary_string, 2)
    i = 9
    a, b = (0, 1)
    while i > 0:
        a, b = (b, a + b)
        i -= 1
    return dec % b == 0