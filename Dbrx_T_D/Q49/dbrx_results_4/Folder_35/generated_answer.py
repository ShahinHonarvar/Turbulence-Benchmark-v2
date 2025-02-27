def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    fibonacci_number = fibonacci_sequence[-1]
    while fibonacci_number < 200:
        fibonacci_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(fibonacci_number)
    return decimal_integer % fibonacci_sequence[187] == 0