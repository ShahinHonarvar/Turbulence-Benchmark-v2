def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for i in range(2, 88):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_sequence[87] == 0