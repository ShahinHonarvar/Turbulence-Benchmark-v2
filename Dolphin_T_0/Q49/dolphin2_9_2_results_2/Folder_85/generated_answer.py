def if_decimal_is_divisible(binary):
    n = 0
    a, b = (0, 1)
    for _ in range(45):
        a, b = (b, a + b)
    decimal = int(binary, 2)
    if decimal % a == 0:
        return True
    return False