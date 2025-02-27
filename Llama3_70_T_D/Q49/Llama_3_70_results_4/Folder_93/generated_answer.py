def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 59:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal = int(binary_string, 2)
    return decimal % fib_sequence[58] == 0