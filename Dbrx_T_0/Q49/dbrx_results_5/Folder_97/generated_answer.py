def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(112):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    target_fibonacci_number = fibonacci_sequence[113]
    if decimal_integer % target_fibonacci_number == 0:
        return True
    else:
        return False