def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_integer = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 100:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_integer % fibonacci_numbers[100] == 0