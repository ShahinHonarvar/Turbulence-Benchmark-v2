def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    while len(fib_seq) < 97:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    divisible_by_97th_fib = int(binary_string, 2) % fib_seq[96] == 0
    return divisible_by_97th_fib