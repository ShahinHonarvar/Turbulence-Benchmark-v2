def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_seq = [0, 1]
    for i in range(2, 19):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_num = fib_seq[-1]
    return decimal_num % fib_num == 0