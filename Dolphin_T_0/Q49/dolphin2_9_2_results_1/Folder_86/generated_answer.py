def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    m = 135
    a, b = (0, 1)
    for _ in range(2, m + 1):
        a, b = (b, a + b)
    return n % b == 0