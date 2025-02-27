def is_decimal_divisible_by_13th_fib(binary_str):
    decimal_num = int(binary_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 13:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_num % fib_sequence[12] == 0