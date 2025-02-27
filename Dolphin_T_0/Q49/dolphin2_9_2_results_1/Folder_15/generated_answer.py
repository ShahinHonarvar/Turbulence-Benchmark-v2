def if_decimal_is_divisible(binary):
    index = 0
    fib_sequence = [0, 1]
    while index < 9:
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
        index += 1
    decimal = int(binary, 2)
    if decimal % fib_sequence[9] == 0:
        return True
    else:
        return False