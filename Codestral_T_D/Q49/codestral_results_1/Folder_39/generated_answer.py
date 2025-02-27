def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 15:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_15 = fib_seq[14]
    decimal = int(binary_str, 2)
    return decimal % fib_15 == 0