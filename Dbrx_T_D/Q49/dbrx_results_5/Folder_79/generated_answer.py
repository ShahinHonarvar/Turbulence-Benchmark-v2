def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)
    fib_seq = [0, 1]
    while fib_seq[-1] < decimal_num:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if decimal_num % fib_seq[13] == 0:
        return True
    else:
        return False