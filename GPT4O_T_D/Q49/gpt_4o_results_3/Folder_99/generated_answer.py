def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 110):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    target_fib_number = fibonacci_sequence[109]
    decimal_integer = int(binary_string, 2)
    return decimal_integer % target_fib_number == 0