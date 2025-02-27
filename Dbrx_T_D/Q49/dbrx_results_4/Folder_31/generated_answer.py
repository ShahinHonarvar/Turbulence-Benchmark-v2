def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 69 or fibonacci_sequence[-1] + fibonacci_sequence[-2] < decimal_number:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_number % fibonacci_sequence[-1] == 0 and fibonacci_sequence[-1] != 0