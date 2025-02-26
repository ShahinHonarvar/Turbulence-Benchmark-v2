def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 14:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fourteenth_fib = fib_sequence[13]
    return decimal_value % fourteenth_fib == 0