def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_seq = [0, 1]
    for i in range(2, 110):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return decimal_num % fib_seq[110 - 1] == 0