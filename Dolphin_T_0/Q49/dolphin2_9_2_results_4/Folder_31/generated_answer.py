def if_decimal_is_divisible(binary):
    index = 69
    a, b = (0, 1)
    for _ in range(index):
        a, b = (b, a + b)
    return int(binary, 2) % b == 0