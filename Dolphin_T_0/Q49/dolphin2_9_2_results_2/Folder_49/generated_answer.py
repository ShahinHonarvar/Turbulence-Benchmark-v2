def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 95:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal_num % fib_seq[94] == 0