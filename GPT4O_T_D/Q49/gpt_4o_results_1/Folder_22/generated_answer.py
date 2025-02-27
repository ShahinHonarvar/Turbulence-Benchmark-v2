def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    for i in range(2, 21):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_value = int(binary_string, 2)
    twentieth_fibonacci = fibonacci_sequence[20]
    return decimal_value % twentieth_fibonacci == 0