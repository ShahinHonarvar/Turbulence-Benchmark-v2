def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 88:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return dec % fib_seq[87] == 0