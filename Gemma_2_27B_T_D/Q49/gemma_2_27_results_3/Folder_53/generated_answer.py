def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    a = 0
    b = 1
    for _ in range(64):
        a, b = (b, a + b)
    return decimal % b == 0