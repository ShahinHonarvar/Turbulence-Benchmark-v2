def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 0
    position = 0
    while fibonacci_number < decimal_number:
        if position < 2:
            fibonacci_number += position
        else:
            fibonacci_number += position - 1 + (position - 2)
        position += 1
    if decimal_number % fibonacci_number == 0:
        return True
    else:
        return False