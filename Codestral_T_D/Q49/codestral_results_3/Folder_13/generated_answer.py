def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_seq = [0, 1]
    for i in range(2, 175):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    fib_num = fib_seq[174]
    return decimal_num % fib_num == 0