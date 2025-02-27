def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < decimal_num:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_num % fibonacci_sequence[94] == 0