def if_decimal_is_divisible(n):
    a, b = (0, 1)
    for _ in range(153):
        a, b = (b, a + b)
    c = int(n, 2) % b
    return c == 0