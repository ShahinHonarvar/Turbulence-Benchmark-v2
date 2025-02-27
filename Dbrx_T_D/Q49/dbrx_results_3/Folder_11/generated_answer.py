def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_number = 16 ** (len(binary_string) - 1)
    if decimal_integer % fibonacci_number == 0:
        return True
    else:
        return False