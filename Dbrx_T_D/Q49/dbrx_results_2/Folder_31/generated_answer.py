def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_69 = fibonacci_sequence(10 ** 5)[68]
    return decimal_integer % fibonacci_69 == 0

def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence