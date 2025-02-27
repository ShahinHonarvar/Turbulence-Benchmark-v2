def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_84 = 700747102616
    return decimal_value % fibonacci_84 == 0