def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fib_sequence = [0, 1]
    for i in range(2, 69):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return n % fib_sequence[68] == 0