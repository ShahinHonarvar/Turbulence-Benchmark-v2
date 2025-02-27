def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = 0
    previous_number = 0
    current_number = 1
    for _ in range(134):
        fibonacci_number = current_number + previous_number
        previous_number = current_number
        current_number = fibonacci_number
    return decimal_number % fibonacci_number == 0