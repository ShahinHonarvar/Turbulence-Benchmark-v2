def is_decimal_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 195:
        next_fibonacci_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci_number)
    target_number = fibonacci_sequence[194]
    remainder = decimal_number % target_number
    if remainder == 0:
        return True
    else:
        return False