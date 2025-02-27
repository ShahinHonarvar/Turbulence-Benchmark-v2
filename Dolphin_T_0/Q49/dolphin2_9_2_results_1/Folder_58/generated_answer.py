def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    n = 0
    a, b = (0, 1)
    while n < 104:
        a, b = (b, a + b)
        n += 1
    return decimal % b == 0