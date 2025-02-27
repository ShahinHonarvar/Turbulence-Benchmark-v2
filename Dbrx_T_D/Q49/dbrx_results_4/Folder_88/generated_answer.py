def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = 0
    previous_number = -1
    current_number = 1
    while fibonacci_number < decimal_number:
        next_number = previous_number + current_number
        previous_number = current_number
        current_number = next_number
        fibonacci_number = current_number
    return fibonacci_number % 49 == 0