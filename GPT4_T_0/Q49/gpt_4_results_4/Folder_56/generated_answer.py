def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_sequence = [0, 1]
    for i in range(2, 84):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    if decimal % fib_sequence[83] == 0:
        return True
    else:
        return False