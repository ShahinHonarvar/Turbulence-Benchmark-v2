def if_decimal_is_divisible(bin_str):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 167):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_number = int(bin_str, 2)
    return decimal_number % fibonacci_sequence[166] == 0