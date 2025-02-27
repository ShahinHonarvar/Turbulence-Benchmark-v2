def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_84 = 0
    fibonacci_83 = 1
    if decimal_representation == 0:
        return True
    for i in range(2, 84 + 1):
        fibonacci_i = fibonacci_83 + fibonacci_84
        fibonacci_83 = fibonacci_84
        fibonacci_84 = fibonacci_i
    if fibonacci_84 != 0 and decimal_representation % fibonacci_84 == 0:
        return True
    else:
        return False