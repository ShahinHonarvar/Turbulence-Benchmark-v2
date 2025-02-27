def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    for _ in range(2, 75):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_sequence[74] == 0