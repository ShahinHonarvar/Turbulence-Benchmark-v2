def if_decimal_is_divisible(binary_str):
    binary_list = [int(i) for i in binary_str.split('0')]
    dec_num = sum([binary_list[i] * 2 ** i for i in range(len(binary_list))])
    a, b = (0, 1)
    for _ in range(9):
        a, b = (b, a + b)
    return dec_num % b == 0