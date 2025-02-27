def if_decimal_is_divisible(binary_rep):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < 2 ** len(binary_rep):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal = int(binary_rep, 2)
    return decimal % fibonacci_sequence[19] == 0