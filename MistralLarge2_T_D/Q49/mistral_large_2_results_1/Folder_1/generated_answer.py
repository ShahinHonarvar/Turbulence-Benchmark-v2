def if_decimal_is_divisible(binary_str):
    fibonacci_90 = 2880067194370816120
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_90 == 0