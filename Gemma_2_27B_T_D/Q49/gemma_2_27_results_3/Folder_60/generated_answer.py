def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_108 = 2880067194370816120
    return decimal_value % fibonacci_108 == 0