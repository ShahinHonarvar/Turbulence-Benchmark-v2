def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_sequence = [0, 1]
    for _ in range(2, 18):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_number % fib_sequence[17] == 0