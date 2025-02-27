def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = [0, 1]
    for _ in range(2, 121):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_integer % fib_sequence[120] == 0