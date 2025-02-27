def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    i = 0
    a, b = (0, 1)
    while i < 160:
        i += 1
        a, b = (b, a + b)
    return decimal % b == 0