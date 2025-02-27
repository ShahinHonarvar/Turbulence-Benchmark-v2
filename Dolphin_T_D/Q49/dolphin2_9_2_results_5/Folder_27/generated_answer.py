def if_decimal_is_divisible(binary_rep):
    index = 86
    a, b = (0, 1)
    while index != 0:
        a, b = (b, a + b)
        index -= 1
    decimal = int(binary_rep, 2)
    if decimal % b == 0:
        return True
    else:
        return False