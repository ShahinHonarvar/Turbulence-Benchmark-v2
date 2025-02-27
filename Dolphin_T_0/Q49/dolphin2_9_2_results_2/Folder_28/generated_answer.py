def if_decimal_is_divisible(bin_num):
    decimal = int(bin_num, 2)
    a, b = (0, 1)
    for _ in range(103):
        a, b = (b, a + b)
    return decimal % a == 0