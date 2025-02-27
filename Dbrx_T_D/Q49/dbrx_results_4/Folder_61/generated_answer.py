def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < 76:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_integer % fibonacci_sequence[-1] == 0