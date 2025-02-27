def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_76 = 88747416986784
    if decimal_number % fibonacci_76 == 0:
        return True
    else:
        return False