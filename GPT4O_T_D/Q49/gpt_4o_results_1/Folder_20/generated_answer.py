def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 101):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_sequence[100] == 0