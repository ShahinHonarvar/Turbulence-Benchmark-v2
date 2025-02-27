def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_15 = 610
    if decimal % fibonacci_15 == 0:
        return True
    else:
        return False