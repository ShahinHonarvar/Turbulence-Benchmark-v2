def if_decimal_is_divisible(binary_str):
    fib_seq = [0, 1]
    for _ in range(2, 189):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_seq[188] == 0