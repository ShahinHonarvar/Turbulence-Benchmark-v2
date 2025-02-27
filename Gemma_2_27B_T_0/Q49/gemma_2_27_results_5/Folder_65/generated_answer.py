def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_127 = 1062882440175024019715778878976
    return decimal_number % fibonacci_127 == 0