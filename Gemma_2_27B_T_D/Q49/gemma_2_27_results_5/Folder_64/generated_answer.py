def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_10th = 55
    if decimal_number % fibonacci_10th == 0:
        return True
    else:
        return False