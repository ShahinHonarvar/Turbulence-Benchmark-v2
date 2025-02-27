def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 168:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_number = fib_sequence[-1]
    return decimal % fib_number == 0