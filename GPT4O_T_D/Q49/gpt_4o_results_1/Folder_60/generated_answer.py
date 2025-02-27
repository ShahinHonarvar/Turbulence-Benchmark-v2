def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 109:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    number_in_decimal = int(binary_string, 2)
    return number_in_decimal % fibonacci_sequence[108] == 0