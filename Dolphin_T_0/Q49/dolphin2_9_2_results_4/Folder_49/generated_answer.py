def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_95 = get_fibonacci_sequence(95)
    return decimal % fibonacci_95 == 0

def get_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[-1]