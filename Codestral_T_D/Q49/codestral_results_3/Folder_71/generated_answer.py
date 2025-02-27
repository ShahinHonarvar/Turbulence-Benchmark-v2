def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 148:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return int(binary_str, 2) % fib_seq[147] == 0