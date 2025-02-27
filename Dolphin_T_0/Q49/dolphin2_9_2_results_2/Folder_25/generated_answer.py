def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_sequence = [0, 1]
    while fib_sequence[-1] < decimal:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-19] != 0 and decimal % fib_sequence[-19] == 0