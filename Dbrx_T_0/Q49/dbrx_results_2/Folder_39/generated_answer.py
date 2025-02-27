def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 15
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < fibonacci_number:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if decimal_number % fibonacci_sequence[fibonacci_number - 1] == 0:
        return True
    else:
        return False