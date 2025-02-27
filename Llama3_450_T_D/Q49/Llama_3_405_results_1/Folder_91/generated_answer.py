def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    decimal = int(binary_str, 2)
    return decimal % fibonacci_sequence[5] == 0