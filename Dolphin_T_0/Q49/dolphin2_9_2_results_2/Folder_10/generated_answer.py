def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= 88:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    return decimal_num % fibonacci_sequence[-1] == 0