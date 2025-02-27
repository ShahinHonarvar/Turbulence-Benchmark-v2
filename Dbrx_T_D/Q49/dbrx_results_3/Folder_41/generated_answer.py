def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 67:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    target_fibonacci_number = fibonacci_sequence[66]
    if decimal_number % target_fibonacci_number == 0:
        return True
    else:
        return False