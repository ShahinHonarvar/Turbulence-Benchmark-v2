def is_decimal_divisible_by_fibonacci(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_integer:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if fibonacci_sequence[-1] == 176:
        fibonacci_sequence.pop()
    if decimal_integer % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False