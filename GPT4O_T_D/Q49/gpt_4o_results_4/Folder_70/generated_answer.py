def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(2, 137 + 1):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fib_137 = fibonacci_sequence[137]
    return decimal_number % fib_137 == 0