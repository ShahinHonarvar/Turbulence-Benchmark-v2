def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 97:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fibonacci_number = fibonacci_sequence[96]
    return decimal_integer % fibonacci_number == 0