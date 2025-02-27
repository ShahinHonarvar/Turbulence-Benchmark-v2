def if_decimal_is_divisible(bin_str):
    num_fibonacci = 39
    dec_num = int(bin_str, 2)
    fibonacci = []
    a, b = (0, 1)
    while len(fibonacci) < num_fibonacci:
        fibonacci.append(a)
        a, b = (b, a + b)
    if dec_num % fibonacci[-1] == 0:
        return True
    else:
        return False