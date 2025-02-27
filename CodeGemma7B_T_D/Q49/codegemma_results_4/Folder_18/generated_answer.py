def if_decimal_is_divisible(binary_representation):
    fib_sequence = [0]
    n = 1
    while True:
        next_number = fib_sequence[n - 1] + fib_sequence[n - 2]
        fib_sequence.append(next_number)
        if next_number > 198 * fib_sequence[n]:
            break
        n += 1
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fib_sequence[198] == 0