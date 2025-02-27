def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    fibonacci_number = 0
    for i in range(10):
        fibonacci_number = fibonacci_number + fibonacci_number
    if decimal_representation % fibonacci_number == 0:
        return True
    else:
        return False