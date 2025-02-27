def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 29:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_value % fibonacci_sequence[27] == 0