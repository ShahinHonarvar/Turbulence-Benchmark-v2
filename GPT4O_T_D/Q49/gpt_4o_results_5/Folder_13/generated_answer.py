def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 174):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fib_174 = fibonacci_sequence[173]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_174 == 0