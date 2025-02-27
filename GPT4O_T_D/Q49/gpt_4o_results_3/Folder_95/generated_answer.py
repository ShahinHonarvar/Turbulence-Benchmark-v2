def if_decimal_is_divisible(binary_representation):
    fib_sequence = [0, 1]
    for _ in range(166):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_number = int(binary_representation, 2)
    return decimal_number % fib_sequence[168] == 0