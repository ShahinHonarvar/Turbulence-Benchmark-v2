def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_number:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if fibonacci_sequence[-1] > decimal_number:
        fibonacci_sequence.pop()
    if fibonacci_sequence[96] == 0:
        fibonacci_sequence[96] = 1
    else:
        fibonacci_sequence[96] += 1
    if decimal_number % fibonacci_sequence[96] == 0:
        return True
    else:
        return False