def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    return decimal % fibonacci_sequence[3] == 0