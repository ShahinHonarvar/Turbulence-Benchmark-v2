def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 30:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_seq[29] == 0