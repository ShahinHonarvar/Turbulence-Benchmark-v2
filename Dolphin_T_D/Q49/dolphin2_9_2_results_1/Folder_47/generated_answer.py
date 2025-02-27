def if_decimal_is_divisible(binary):
    n = 0
    a, b = (0, 1)
    while n < 94:
        a, b = (b, a + b)
        n += 1
    decimal = int(binary, 2)
    if decimal % b == 0:
        return True
    else:
        return False