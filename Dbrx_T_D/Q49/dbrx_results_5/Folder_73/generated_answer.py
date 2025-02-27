def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 164:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if decimal_integer % fib_sequence[163] == 0:
        return True
    else:
        return False