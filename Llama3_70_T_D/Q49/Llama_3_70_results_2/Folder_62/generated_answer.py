def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 130:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_130 = fib_sequence[129]
    decimal = int(binary_str, 2)
    return decimal % fib_130 == 0