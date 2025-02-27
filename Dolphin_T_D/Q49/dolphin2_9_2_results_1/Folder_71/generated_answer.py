def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    m, k = (0, 1)
    for i in range(146):
        m, k = (k, m + k)
    return n % m == 0