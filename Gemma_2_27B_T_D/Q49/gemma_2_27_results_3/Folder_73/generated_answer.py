def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_164 = 37414307124379963783
    return decimal_number % fibonacci_164 == 0