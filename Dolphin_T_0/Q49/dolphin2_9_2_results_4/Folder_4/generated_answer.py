def if_decimal_is_divisible(binary_rep):
    i117 = 0
    i118 = 1
    fib = [0, 1]
    while len(fib) < 118:
        i117, i118 = (i118, i117 + i118)
        fib.append(i117)
    dec_val = int(binary_rep, 2)
    if dec_val % fib[117] == 0:
        return True
    else:
        return False