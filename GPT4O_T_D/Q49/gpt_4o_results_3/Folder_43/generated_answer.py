def if_decimal_is_divisible(binary_str):
    n_decimal = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(76):
        a, b = (b, a + b)
    return n_decimal % b == 0