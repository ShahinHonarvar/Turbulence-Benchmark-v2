def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_168 = 19982885270794498816
    return decimal % fibonacci_168 == 0