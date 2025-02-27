def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] < 77:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if fibonacci_sequence[-1] % 77 == 0 and decimal_integer % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False