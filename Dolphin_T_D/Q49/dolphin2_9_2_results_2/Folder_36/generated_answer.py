def if_decimal_is_divisible(binary_str):
    n_fib = 150
    decimal = int(binary_str, 2)
    fib_sequence = [0, 1]
    for _ in range(2, n_fib + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    n_fib_value = fib_sequence[n_fib]
    return decimal % n_fib_value == 0