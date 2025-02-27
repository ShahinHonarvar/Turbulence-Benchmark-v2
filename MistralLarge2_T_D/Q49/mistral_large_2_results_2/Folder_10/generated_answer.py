def if_decimal_is_divisible(binary_representation):
    if not binary_representation:
        return False
    decimal = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 88:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal % fibonacci_sequence[88] == 0