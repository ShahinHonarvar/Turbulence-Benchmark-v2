def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    a, b = (0, 1)
    fibonacci_sequence = [a]
    for _ in range(130):
        a, b = (b, a + b)
        fibonacci_sequence.append(a)
    return decimal_number % fibonacci_sequence[130 - 1] == 0