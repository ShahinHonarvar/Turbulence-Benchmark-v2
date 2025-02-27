def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_74th = 13942322456190
    if decimal_value % fibonacci_74th == 0:
        return True
    else:
        return False