def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci24 = 46368
    return decimal % fibonacci24 == 0