def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    while len(fib_seq) < 10:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal = int(binary_str, 2)
    return decimal % fib_seq[9] == 0