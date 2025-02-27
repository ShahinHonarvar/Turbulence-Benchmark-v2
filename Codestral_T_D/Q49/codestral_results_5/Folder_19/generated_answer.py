def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(str(fib_seq[-1])) < len(binary_str):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_29th = fib_seq[28]
    decimal = int(binary_str, 2)
    return decimal % fib_29th == 0