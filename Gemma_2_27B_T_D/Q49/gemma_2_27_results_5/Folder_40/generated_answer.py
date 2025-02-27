def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_4th = 2
    if decimal % fibonacci_4th == 0:
        return True
    else:
        return False