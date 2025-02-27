def if_decimal_is_divisible(bin_string):
    dec_integer = int(bin_string, 2)
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] < 95:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return dec_integer % fib_seq[94] == 0