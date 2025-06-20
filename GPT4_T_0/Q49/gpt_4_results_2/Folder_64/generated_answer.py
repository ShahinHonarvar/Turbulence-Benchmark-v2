def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 10:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal % fib_sequence[-1] == 0