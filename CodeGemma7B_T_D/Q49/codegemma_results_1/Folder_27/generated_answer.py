def if_decimal_is_divisible(bin_str):
    n = int(bin_str, 2)
    a, b, c = (0, 0, 1)
    for i in range(18):
        a, b, c = (b, c, a + b)
    if n % c == 0:
        return True
    else:
        return False