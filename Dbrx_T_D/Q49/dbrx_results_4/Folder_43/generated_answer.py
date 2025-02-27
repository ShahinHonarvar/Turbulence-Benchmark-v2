def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while True:
        if fibonacci_sequence[-1] + fibonacci_sequence[-2] > 77:
            break
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if len(fibonacci_sequence) < 77:
        return False
    return decimal_integer % fibonacci_sequence[76] == 0