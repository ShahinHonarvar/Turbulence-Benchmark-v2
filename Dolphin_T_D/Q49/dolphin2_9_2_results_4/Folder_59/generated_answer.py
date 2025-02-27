def if_decimal_is_divisible(binary_rep):
    decimal_int = int(binary_rep, 2)
    a, b = (0, 1)
    for _ in range(74):
        a, b = (b, a + b)
    if decimal_int % a == 0:
        return True
    else:
        return False