def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13]
    seventh_fibonacci_number = fibonacci_sequence[7]
    decimal_representation = int(binary_string, 2)
    return decimal_representation % seventh_fibonacci_number == 0