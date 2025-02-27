def if_decimal_is_divisible(binary_rep):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 90:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_number = int(binary_rep, 2)
    return decimal_number % fib_sequence[89] == 0