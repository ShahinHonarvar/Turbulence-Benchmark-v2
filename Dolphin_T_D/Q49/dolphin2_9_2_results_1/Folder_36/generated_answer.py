def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib_sequence = [0, 1]
    for i in range(2, 150):
        fib_sequence.append(fib_sequence[i - 2] + fib_sequence[i - 1])
    return decimal % fib_sequence[149] == 0