def if_decimal_is_divisible(binary_representation):
    fib_sequence = [0, 1]
    for _ in range(2, 81):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_80th = fib_sequence[80]
    decimal_number = int(binary_representation, 2)
    return decimal_number % fib_80th == 0