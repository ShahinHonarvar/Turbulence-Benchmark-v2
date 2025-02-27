def if_decimal_is_divisible(binary):
    a, b = (0, 1)
    i = 0
    while i < 15:
        a, b = (b, a + b)
        i += 1
    decimal = int(binary, 2)
    return decimal % b == 0