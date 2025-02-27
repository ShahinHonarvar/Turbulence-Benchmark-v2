def if_decimal_is_divisible(binary_representation):
    idx = 2
    a, b = (0, 1)
    fibonacci_sequence = [a, b]
    while len(fibonacci_sequence) < 150:
        a, b = (b, a + b)
        fibonacci_sequence.append(b)
        idx += 1
    decimal_number = int(binary_representation, 2)
    return decimal_number % fibonacci_sequence[149] == 0