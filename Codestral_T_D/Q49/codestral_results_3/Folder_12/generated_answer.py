def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 66:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal % fib_seq[65] == 0