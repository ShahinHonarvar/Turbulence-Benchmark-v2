def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 39):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    fib_39th = fibonacci_sequence[38]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_39th == 0