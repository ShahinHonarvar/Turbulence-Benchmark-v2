def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    fibonacci_sequence = [0, 1]
    i = 2
    while fibonacci_sequence[i - 1] < decimal_number:
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
        i += 1
    return decimal_number % fibonacci_sequence[-1] == 0