def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-2] + fibonacci_numbers[-1] < 15:
        fibonacci_numbers.append(fibonacci_numbers[-2] + fibonacci_numbers[-1])
    target_number = fibonacci_numbers[-3]
    return decimal_number % target_number == 0