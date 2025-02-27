def if_decimal_is_divisible(binary_string: str) -> bool:
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 47:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_number % fibonacci_numbers[-1] == 0 and len(fibonacci_numbers) == 47