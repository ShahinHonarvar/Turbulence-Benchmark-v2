def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for i in range(2, 91):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    target_number = fibonacci_sequence[90]
    decimal_number = int(binary_str, 2)
    return decimal_number % target_number == 0