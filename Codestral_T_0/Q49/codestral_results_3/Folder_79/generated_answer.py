def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 13:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_13 = fib_seq[12]
    return decimal % fib_13 == 0