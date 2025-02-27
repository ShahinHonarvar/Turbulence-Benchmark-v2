def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_178 = 8955208090169257603005692418736074727466869867737282917728163
    return decimal_number % fibonacci_178 == 0