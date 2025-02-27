def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 139:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return num % fibonacci_sequence[138] == 0