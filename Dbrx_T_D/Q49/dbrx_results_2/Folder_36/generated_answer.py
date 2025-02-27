def if_decimal_is_divisible(binary_representation: str) -> bool:
    decimal_number = int(binary_representation, 2)
    fibonacci_number = 0
    fib_sequence = [0, 1]
    while fibonacci_number < decimal_number:
        fibonacci_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(fibonacci_number)
    return decimal_number % fib_sequence[150] == 0