def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_64 = 10610209857723
    if decimal_integer % fibonacci_64 == 0:
        return True
    else:
        return False