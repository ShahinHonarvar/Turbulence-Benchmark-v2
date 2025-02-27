def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) <= 97:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    fibonacci_97th = fibonacci_numbers[97]
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_97th == 0