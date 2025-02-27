def if_decimal_is_divisible(binary_number):
    decimal_number = int(binary_number, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 199):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    return decimal_number % fibonacci_sequence[198] == 0