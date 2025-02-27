def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    n = 104
    a, b = (0, 1)
    while n > 1:
        a, b = (b, a + b)
        n -= 1
    if decimal % b == 0:
        return True
    else:
        return False