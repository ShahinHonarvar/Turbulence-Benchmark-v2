def if_decimal_is_divisible(binary):
    index = 127
    fib_sequence = [0, 1]
    while len(fib_sequence) < index:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal = int(binary, 2)
    return fib_sequence[index - 1] != 0 and decimal % fib_sequence[index - 1] == 0