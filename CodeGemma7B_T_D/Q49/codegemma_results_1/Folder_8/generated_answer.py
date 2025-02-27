def if_decimal_is_divisible(binary_representation_string):
    decimal_integer = int(binary_representation_string, 2)
    fibonacci_number = fibonacci(54)
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False