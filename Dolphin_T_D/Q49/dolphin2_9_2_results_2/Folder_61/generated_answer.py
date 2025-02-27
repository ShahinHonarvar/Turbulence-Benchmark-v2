def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    index = 76
    a, b = (0, 1)
    for _ in range(index + 1):
        a, b = (b, a + b)
    return decimal % a == 0