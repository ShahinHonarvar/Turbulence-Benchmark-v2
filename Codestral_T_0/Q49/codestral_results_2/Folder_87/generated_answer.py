def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 180:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_180 = fib_seq[-1]
    return decimal % fib_180 == 0