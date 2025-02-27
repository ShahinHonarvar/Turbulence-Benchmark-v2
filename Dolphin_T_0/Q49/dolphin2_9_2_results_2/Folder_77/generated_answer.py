def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    a, b = (0, 1)
    i = 0
    while i < 110:
        a, b = (b, a + b)
        i += 1
    return decimal % b == 0