def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 17:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_num = fib_seq[16]
    return decimal % fib_num == 0