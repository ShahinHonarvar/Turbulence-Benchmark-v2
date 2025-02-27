def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 77 + 1):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return n % fibonacci_sequence[77] == 0