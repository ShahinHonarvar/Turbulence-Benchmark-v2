def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_integer:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fifteenth_fibonacci = fibonacci_sequence[14]
    if decimal_integer % fifteenth_fibonacci == 0:
        return True
    else:
        return False