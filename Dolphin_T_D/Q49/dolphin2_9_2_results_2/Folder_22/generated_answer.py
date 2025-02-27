def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    for i in range(2, 20):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fib_sequence[19] == 0