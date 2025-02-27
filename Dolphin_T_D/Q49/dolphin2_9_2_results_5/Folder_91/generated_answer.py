def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_6 = ((5 * 5 + 4) / 2) ** 2
    if decimal % fibonacci_6 == 0:
        return True
    else:
        return False