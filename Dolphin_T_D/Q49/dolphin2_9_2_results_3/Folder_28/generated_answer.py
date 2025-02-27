def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0]
    for i in range(1, 105):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    decimal_number = int(binary_representation, 2)
    return decimal_number % fibonacci_sequence[104] == 0