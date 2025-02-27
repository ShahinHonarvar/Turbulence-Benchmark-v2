def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = 102334155
    return decimal_number % fibonacci_number == 0