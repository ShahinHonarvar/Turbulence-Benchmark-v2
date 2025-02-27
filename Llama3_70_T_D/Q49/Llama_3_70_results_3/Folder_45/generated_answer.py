def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 28:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    divisor = fib_sequence[27]
    decimal_value = int(binary_str, 2)
    return decimal_value % divisor == 0