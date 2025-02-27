def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    for _ in range(37):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    divisor = fib_sequence[38]
    decimal = int(binary_string, 2)
    return decimal % divisor == 0