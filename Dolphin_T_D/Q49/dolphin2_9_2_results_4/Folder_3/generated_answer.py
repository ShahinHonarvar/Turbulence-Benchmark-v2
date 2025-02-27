def if_decimal_is_divisible(binary_rep):
    fib_seq = [0, 1]
    while len(fib_seq) < 35:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_rep = int(binary_rep, 2)
    return decimal_rep % fib_seq[34] == 0