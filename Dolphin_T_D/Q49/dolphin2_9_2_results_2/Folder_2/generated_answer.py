def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    a, b = (0, 1)
    for _ in range(124):
        a, b = (b, a + b)
    if decimal % b == 0:
        return True
    else:
        return False