def if_decimal_is_divisible(binary):
    position = len(binary) - 42
    a, b = (0, 1)
    for i in range(position):
        c = a + b
        a, b = (b, c)
    return int(binary, 2) % b == 0 if position >= 0 else True