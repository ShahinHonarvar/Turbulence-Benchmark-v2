def if_decimal_is_divisible(binary_representation):
    binary_to_decimal = int(binary_representation, 2)
    fibonacci_sequence = [0]
    while fibonacci_sequence[-1] < binary_to_decimal / 144 + 1:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[-1] == int(binary_to_decimal / 144)