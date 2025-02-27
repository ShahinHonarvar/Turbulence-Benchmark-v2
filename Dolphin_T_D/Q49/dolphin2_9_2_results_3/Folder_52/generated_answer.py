def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 176:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal_num % fib_seq[175] == 0