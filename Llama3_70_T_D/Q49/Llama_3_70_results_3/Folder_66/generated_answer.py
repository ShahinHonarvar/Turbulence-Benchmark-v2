def if_decimal_is_divisible(s):
    a, b = (0, 1)
    for _ in range(120):
        a, b = (b, a + b)
    return int(s, 2) % b == 0