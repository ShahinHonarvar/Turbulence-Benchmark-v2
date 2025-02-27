def if_decimal_is_divisible(binary_representation):
    n = 147
    fibonacci_sequence = [0, 1]
    for i in range(2, n + 1):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    decimal = int(binary_representation, 2)
    return decimal % fibonacci_sequence[n] == 0