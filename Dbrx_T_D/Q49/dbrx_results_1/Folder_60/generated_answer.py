def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(2, 108):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if decimal_number % fibonacci_sequence[107] == 0:
        return True
    else:
        return False