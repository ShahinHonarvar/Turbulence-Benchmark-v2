def if_decimal_is_divisible(bin_num):
    fib_seq = [0, 1]
    i = 2
    while i < 59:
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        i += 1
    dec_num = int(bin_num, 2)
    return dec_num % fib_seq[58] == 0