def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = generate_fibonacci_sequence(34)
    decimal = int(binary_string, 2)
    return decimal % fibonacci_sequence[34] == 0