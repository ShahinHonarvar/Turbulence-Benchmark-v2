def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 120:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal_num % fib_seq[119] == 0