def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13]
    return decimal % fibonacci_sequence[3] == 0