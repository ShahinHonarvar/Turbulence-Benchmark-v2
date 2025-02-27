def is_decimal_divisible_by_56th_fibonacci(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < decimal_number:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    if len(fibonacci_numbers) < 56:
        return False
    return decimal_number % fibonacci_numbers[55] == 0