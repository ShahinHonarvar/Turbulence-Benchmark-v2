def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    for _ in range(2, 189):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    fib_188th = fib_seq[188]
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_188th == 0