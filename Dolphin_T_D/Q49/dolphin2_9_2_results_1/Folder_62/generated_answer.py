def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 130:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_num % fibonacci_sequence[129] == 0