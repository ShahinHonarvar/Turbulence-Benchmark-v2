def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 109:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return decimal_number % fibonacci_sequence[108] == 0