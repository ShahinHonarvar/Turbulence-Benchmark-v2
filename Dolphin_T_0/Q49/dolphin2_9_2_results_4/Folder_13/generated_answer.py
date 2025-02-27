def if_decimal_is_divisible(binary_rep):
    fibonacci = [0]
    a = b = 1
    while b <= int(binary_rep, 2) * 2:
        fibonacci.append(b)
        a, b = (b, a + b)
    dec_num = int(binary_rep, 2)
    return dec_num % fibonacci[-1] == 0