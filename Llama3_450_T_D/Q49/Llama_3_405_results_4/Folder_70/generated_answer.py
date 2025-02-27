def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 137:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    divisor = fib_sequence[136]
    decimal_number = int(binary_string, 2)
    return decimal_number % divisor == 0