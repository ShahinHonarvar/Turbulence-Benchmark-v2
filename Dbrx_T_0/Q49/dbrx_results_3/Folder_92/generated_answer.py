def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] < decimal_integer:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    seventh_fibonacci_number = fibonacci_sequence[6]
    return decimal_integer % seventh_fibonacci_number == 0