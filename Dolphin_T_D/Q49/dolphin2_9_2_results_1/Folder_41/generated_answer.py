def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    n = 67
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return decimal % b == 0