def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_seq = [0, 1]
    for i in range(2, 155):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return decimal % fib_seq[154] == 0