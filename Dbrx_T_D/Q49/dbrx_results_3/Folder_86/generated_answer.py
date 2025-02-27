def is_decimal_divisible_by_fibonacci(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while True:
        if len(fibonacci_sequence) >= 135:
            break
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    if decimal_integer % fibonacci_sequence[134] == 0:
        return True
    else:
        return False