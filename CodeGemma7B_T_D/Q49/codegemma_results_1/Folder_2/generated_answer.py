def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = 0
    counter = 0
    while counter <= decimal_integer:
        fibonacci_number, counter = (fibonacci_number + counter, fibonacci_number)
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False