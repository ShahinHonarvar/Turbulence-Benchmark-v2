def if_decimal_is_divisible(n):
    a, b = (0, 1)
    for _ in range(66):
        a, b = (b, a + b)
    return int(n, 2) % b == 0