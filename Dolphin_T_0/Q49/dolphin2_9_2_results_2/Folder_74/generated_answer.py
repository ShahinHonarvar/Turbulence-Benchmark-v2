def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fib_seq = [0, 1]
    for i in range(2, 167):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return decimal_num % fib_seq[166] == 0