def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 199:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_199 = fib_sequence[199]
    decimal = int(binary_string, 2)
    return decimal % fib_199 == 0