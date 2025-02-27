def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 29:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal % fib_sequence[29] == 0