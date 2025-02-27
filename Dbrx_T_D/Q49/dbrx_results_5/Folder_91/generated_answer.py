def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = [0, 1]
    while fib_sequence[-1] < decimal_integer:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_integer % fib_sequence[5] == 0