def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    thirteenth_fibonacci = 233
    return decimal_number % thirteenth_fibonacci == 0