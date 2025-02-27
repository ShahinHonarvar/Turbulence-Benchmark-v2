def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    for _ in range(178):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    divisor = fibonacci_sequence[179]
    decimal = int(binary_string, 2)
    return decimal % divisor == 0