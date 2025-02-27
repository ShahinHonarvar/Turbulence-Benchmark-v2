def if_decimal_is_divisible(s):
    a, b = (0, 1)
    for _ in range(180):
        a, b = (b, a + b)
    n = int(s, 2)
    return n % b == 0