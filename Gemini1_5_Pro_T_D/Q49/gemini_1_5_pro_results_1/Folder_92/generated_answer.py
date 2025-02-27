def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13]
    seventh_fibonacci_number = fibonacci_numbers[7]
    if decimal_representation % seventh_fibonacci_number == 0:
        return True
    else:
        return False