def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while True:
        if fibonacci_sequence[-1] + fibonacci_sequence[-2] > decimal_integer:
            break
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if len(fibonacci_sequence) < 67:
        return False
    if decimal_integer % fibonacci_sequence[66] == 0:
        return True
    else:
        return False