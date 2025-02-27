def if_decimal_is_divisible(bin_num):
    dec_num = int(bin_num, 2)
    fib_178 = (5 * (11 ** 0.5 + 27) ** 0.5 - 2 * 11 ** 0.5 - 6) / 10
    if dec_num % fib_178 == 0:
        return True
    else:
        return False