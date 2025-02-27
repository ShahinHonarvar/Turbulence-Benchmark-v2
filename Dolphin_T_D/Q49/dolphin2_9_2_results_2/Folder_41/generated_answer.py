def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_sequence = [0, 1]
    for i in range(2, 67 + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return decimal % fib_sequence[66] == 0