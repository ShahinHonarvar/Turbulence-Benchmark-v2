def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for n in range(2, 301):
        fib_sequence.append(fib_sequence[n - 1] + fib_sequence[n - 2])
    if int(binary_str, 2) % fib_sequence[166] == 0:
        return True
    else:
        return False