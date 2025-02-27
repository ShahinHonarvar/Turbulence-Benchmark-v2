def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_90 = 2880067194370816120
    return decimal_number % fibonacci_90 == 0