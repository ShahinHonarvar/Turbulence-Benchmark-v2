def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 179:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    target_fibonacci_number = fibonacci_sequence[178]
    return decimal_integer % target_fibonacci_number == 0