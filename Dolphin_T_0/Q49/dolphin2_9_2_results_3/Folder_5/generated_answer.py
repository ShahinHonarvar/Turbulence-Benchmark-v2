def if_decimal_is_divisible(binary_string):
    decimal_number = int('0b' + binary_string, 2)
    a, b = (0, 1)
    index = 0
    while index < 85:
        a, b = (b, a + b)
        index += 1
    is_divisible = decimal_number % b == 0
    return is_divisible