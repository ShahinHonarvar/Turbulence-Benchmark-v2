def if_decimal_is_divisible(binary_rep):
    decimal_value = int(binary_rep, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 151:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_value % fib_sequence[150] == 0