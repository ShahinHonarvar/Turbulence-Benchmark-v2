def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 40):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_sequence[39] == 0