def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_88 = 1320787
    if decimal_number % fibonacci_88 == 0:
        return True
    else:
        return False