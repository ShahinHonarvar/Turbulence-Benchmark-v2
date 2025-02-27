def is_decimal_divisible_by_fibonacci(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 178):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal_integer % fibonacci_sequence[176] == 0:
        return True
    else:
        return False