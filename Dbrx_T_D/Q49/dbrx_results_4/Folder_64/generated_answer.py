def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = 34

    def fibonacci_sequence(current, length):
        sequence = [current]
        while len(sequence) < length:
            current, sequence[-1] = (current + sequence[-1], current)
        return sequence
    fibonacci_numbers = fibonacci_sequence(0, 10)
    return decimal_integer % fibonacci_number == 0