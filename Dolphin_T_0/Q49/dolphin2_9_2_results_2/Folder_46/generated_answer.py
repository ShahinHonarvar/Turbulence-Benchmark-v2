def if_decimal_is_divisible(binary_rep):
    a, b = (0, 1)
    for _ in range(139):
        a, b = (b, a + b)
    decimal_number = int(binary_rep, 2)
    if decimal_number % b == 0:
        return True
    else:
        return False