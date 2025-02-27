def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_index = 80
    fibonacci_sequence = [0, 1]
    if fibonacci_index > len(fibonacci_sequence):
        for i in range(2, fibonacci_index + 1):
            fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if fibonacci_sequence[fibonacci_index] > decimal_integer:
        return False
    if decimal_integer % fibonacci_sequence[fibonacci_index] == 0:
        return True
    else:
        return False