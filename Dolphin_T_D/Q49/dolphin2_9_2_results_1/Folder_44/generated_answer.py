def if_decimal_is_divisible(binary_rep):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 159:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fib_159 = fibonacci_sequence[158]
    decimal = int(binary_rep, 2)
    return decimal % fib_159 == 0