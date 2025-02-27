def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    tenth_fibonacci = 34
    return decimal_number % tenth_fibonacci == 0