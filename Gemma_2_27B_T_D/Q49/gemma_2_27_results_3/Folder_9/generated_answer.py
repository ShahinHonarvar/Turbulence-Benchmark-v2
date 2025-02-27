def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_68th = 2971215073
    if decimal % fibonacci_68th == 0:
        return True
    else:
        return False