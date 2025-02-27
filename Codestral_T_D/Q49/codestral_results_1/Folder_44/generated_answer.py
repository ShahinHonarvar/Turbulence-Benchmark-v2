def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 159:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal % fib_seq[158] == 0