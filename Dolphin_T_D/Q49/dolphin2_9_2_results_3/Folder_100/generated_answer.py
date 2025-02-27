def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    fibonacci_sequence = []
    a, b = (0, 1)
    while len(fibonacci_sequence) < 190:
        fibonacci_sequence.append(a)
        a, b = (b, a + b)
    return decimal_number % fibonacci_sequence[189] == 0