def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 197:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if decimal_number % fib_sequence[196] == 0:
        return True
    else:
        return False