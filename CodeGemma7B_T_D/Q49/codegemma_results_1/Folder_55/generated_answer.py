def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    fibonacci_sequence = [0]
    for i in range(1, 40):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal_int % fibonacci_sequence[38] == 0:
        return True
    else:
        return False