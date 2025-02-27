def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_20 = 6765
    if decimal_number % fibonacci_20 == 0:
        return True
    else:
        return False