def if_decimal_is_divisible(bin_str):
    fib_sequence = [0, 1]
    for _ in range(2, 56):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_number = int(bin_str, 2)
    return decimal_number % fib_sequence[55] == 0