def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 199):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fibonacci_199 = fibonacci_sequence[-1]
    decimal_number = int(binary_representation, 2)
    return decimal_number % fibonacci_199 == 0