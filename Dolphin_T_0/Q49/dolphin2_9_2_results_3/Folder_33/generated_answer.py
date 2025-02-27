def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    n = 134
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_num % fib_sequence[n - 1] == 0