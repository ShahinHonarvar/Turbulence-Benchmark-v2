def if_decimal_is_divisible(binary_rep):
    n = 0
    a, b = (0, 1)
    while n < 34:
        a, b = (b, a + b)
        n += 1
    dec_num = int(binary_rep, 2)
    return dec_num % b == 0