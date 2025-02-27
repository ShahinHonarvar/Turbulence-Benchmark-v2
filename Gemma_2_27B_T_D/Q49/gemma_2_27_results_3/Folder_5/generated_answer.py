def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_85 = 232792560
    if decimal_value % fibonacci_85 == 0:
        return True
    else:
        return False