def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 24):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    division_result = n // fibonacci_sequence[23]
    return division_result * fibonacci_sequence[23] == n