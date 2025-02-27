def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    a, b = (0, 1)
    for _ in range(159):
        a, b = (b, a + b)
    return n % b == 0