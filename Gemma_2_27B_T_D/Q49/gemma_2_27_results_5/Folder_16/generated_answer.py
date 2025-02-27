def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_128 = 193492367768045154824974595173418346678549323324713102321
    return decimal_integer % fibonacci_128 == 0