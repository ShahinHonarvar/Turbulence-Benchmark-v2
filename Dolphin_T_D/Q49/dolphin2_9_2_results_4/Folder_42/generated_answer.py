def if_decimal_is_divisible(binary_number):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 147:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return int(binary_number, 2) % fib_sequence[146] == 0