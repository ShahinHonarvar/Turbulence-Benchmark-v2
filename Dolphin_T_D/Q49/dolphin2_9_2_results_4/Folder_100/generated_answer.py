def if_decimal_is_divisible(bin_str):
    index = 190
    a, b = (0, 1)
    for _ in range(index - 1):
        a, b = (b, a + b)
    dec_num = int(bin_str, 2)
    return dec_num % a == 0