def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_sequence = [0, 1]
    n = 2
    while len(fib_sequence) < 7:
        fib_sequence.append(fib_sequence[n - 2] + fib_sequence[n - 1])
        n += 1
    seventh_fib_number = fib_sequence[6]
    if decimal % seventh_fib_number == 0:
        return True
    else:
        return False