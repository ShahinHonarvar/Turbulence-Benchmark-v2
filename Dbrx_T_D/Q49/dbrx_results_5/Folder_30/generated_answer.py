def is_fibonacci_number_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < decimal_number:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_number % fibonacci_numbers[186] == 0