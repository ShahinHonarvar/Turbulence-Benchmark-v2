def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_sequence = [0, 1]
    for i in range(2, 175):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return decimal % fib_sequence[173] == 0