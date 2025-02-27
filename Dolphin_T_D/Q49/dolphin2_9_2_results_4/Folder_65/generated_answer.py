def if_decimal_is_divisible(binary_string):
    decimal_val = int(binary_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 127:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if decimal_val % fib_seq[126] == 0:
        return True
    else:
        return False