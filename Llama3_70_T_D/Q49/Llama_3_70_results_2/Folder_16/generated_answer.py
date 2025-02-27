def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    for i in range(2, 128):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    divisor = fib_sequence[127]
    decimal = int(binary_string, 2)
    return decimal % divisor == 0