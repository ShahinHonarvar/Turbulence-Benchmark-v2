def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(5):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return n % fibonacci_sequence[5] == 0