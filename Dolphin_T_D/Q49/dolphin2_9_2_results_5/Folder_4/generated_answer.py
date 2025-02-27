def if_decimal_is_divisible(binary_rep):
    i = 0
    a = 0
    b = 1
    while i < 118:
        a, b = (b, a + b)
        i += 1
    decimal = int(binary_rep, 2)
    if decimal % b == 0:
        return True
    return False