def if_decimal_is_divisible(binary_int):
    a, b = (0, 1)
    count = 0
    while count < 95:
        a, b = (b, a + b)
        count += 1
    dec_int = int(binary_int, 2)
    return dec_int % b == 0