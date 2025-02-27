def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 177:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_176 = fib_sequence[176]
    decimal = int(binary_str, 2)
    return decimal % fib_176 == 0