def if_decimal_is_divisible(binary_rep):
    fib_seq = [0, 1]
    while len(fib_seq) < 84:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_num = fib_seq[-1]
    decimal_num = int(binary_rep, 2)
    return decimal_num % fib_num == 0