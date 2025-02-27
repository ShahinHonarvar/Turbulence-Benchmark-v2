def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_16 = fibonacci_sequence(16)
    if decimal_integer % fibonacci_16 == 0:
        return True
    else:
        return False

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[-1]