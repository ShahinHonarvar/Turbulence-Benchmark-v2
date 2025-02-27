def if_decimal_is_divisible(binary_rep):
    index = 67
    fib_sequence = [0, 1]
    while index >= len(fib_sequence):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_num = int(binary_rep, 2)
    return decimal_num % fib_sequence[index] == 0