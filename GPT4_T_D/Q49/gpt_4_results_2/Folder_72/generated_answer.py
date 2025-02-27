def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    a, b = (0, 1)
    for _ in range(175):
        a, b = (b, a + b)
    return n % a == 0