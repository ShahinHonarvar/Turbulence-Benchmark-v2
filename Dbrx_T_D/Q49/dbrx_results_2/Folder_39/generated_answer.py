def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = 0
    previous_number = -1
    while fibonacci_number < 15:
        fibonacci_number, previous_number = (fibonacci_number + previous_number, fibonacci_number)
    return decimal_integer % fibonacci_number == 0