def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_integer:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if len(fibonacci_sequence) < 138:
        return False
    divisor = fibonacci_sequence[137]
    return decimal_integer % divisor == 0