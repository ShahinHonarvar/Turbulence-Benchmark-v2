def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 126):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal % fibonacci_sequence[125] == 0:
        return True
    else:
        return False