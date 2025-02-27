def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < 110:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if decimal_integer % fibonacci_sequence[109] == 0:
        return True
    else:
        return False