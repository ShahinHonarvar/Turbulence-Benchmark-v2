def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 39:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_39 = fib_sequence[38]
    decimal = int(binary_string, 2)
    return decimal % fib_39 == 0