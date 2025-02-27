def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 137:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_number = fib_sequence[136]
    if decimal_integer % fib_number == 0:
        return True
    else:
        return False