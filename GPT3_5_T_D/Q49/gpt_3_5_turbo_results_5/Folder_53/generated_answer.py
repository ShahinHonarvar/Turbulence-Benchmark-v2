def if_decimal_is_divisible(binary):
    fib_sequence = [0, 1]
    for i in range(2, 65):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    decimal = int(binary, 2)
    if decimal % fib_sequence[63] == 0:
        return True
    else:
        return False