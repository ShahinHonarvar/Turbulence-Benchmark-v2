def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    i = 9
    fib_sequence = [0, 1]
    while len(fib_sequence) <= i:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal % fib_sequence[i - 1] == 0