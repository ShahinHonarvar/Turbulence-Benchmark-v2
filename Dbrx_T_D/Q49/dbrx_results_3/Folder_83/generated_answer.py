def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > decimal_integer:
            break
        fib_sequence.append(next_fib)
    if decimal_integer % fib_sequence[60] == 0:
        return True
    else:
        return False