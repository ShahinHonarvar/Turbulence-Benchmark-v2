def is_integer_divisible_by_68th_fibonacci_number(binary_string):
    decimal_integer = int(binary_string, 2)
    if decimal_integer < 0:
        raise ValueError('Input must be a binary representation of a non-negative decimal integer')
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 68:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    target_fibonacci_number = fibonacci_sequence[67]
    if decimal_integer % target_fibonacci_number == 0:
        return True
    else:
        return False