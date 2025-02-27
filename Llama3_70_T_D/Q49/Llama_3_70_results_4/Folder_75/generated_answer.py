def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def decimal_from_binary(binary):
    return int(binary, 2)

def if_decimal_is_divisible(binary):
    fib_sequence = fibonacci_sequence(190)
    decimal = decimal_from_binary(binary)
    return decimal % fib_sequence[189] == 0