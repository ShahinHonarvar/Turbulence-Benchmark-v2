def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_166 = 1.063163744127966e+35
    if decimal_number % fibonacci_166 == 0:
        return True
    else:
        return False