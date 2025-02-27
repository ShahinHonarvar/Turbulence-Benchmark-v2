def is_fibonacci_number_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_number:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if decimal_number % fibonacci_sequence[133] == 0:
        return True
    else:
        return False