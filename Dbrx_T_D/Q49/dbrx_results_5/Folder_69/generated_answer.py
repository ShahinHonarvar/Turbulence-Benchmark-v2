def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_number = 0
    for _ in range(170):
        fibonacci_number, _ = fibonacci_number + _ or (0, 1)
    return decimal_number % fibonacci_number == 0