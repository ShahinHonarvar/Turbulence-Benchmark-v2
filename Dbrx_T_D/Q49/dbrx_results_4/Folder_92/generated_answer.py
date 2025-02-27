def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < decimal_number:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_number % fibonacci_numbers[6] == 0