def is_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(102):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    target_number = fibonacci_sequence[103]
    return decimal_number % target_number == 0