def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number % 3 == 0