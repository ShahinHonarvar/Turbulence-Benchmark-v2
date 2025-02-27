def if_decimal_is_divisible(binary_str):
    dec_val = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(179):
        a, b = (b, a + b)
    return dec_val % b == 0