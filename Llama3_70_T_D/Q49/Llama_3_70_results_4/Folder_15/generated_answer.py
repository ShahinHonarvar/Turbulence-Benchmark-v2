def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 9:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    ninth_fibonacci_number = fibonacci_sequence[8]
    decimal_integer = int(binary_string, 2)
    return decimal_integer % ninth_fibonacci_number == 0