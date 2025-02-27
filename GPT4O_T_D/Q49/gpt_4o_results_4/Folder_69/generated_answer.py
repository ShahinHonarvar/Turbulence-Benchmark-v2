def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 171):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fib_170 = fibonacci_sequence[170]
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_170 == 0