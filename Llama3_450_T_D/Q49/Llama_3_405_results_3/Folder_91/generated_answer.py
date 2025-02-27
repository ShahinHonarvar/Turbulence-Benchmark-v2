def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 6:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_num % fib_sequence[5] == 0