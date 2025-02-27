def if_decimal_is_divisible(binary_number):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= 146:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    divisor = fibonacci_sequence[146]
    decimal_number = int(binary_number, 2)
    return decimal_number % divisor == 0