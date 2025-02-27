def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_59 = 577831286886426173128
    return decimal_value % fibonacci_59 == 0