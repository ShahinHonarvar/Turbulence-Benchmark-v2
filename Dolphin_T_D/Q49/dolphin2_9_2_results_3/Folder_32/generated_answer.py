def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    Fibonacci_sequence = [0, 1]
    while len(Fibonacci_sequence) < 178:
        Fibonacci_sequence.append(Fibonacci_sequence[-2] + Fibonacci_sequence[-1])
    return decimal_number % Fibonacci_sequence[177] == 0