def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = 0
    previous_number = -1
    current_number = 0
    for _ in range(166):
        if fibonacci_number == 0 or fibonacci_number == 1:
            fibonacci_number = fibonacci_number + previous_number
            previous_number = fibonacci_number - previous_number
        else:
            next_number = fibonacci_number + previous_number
            previous_number = fibonacci_number
            fibonacci_number = next_number
    return decimal_number % fibonacci_number == 0