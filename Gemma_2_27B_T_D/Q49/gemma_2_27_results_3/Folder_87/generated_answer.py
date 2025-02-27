def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_180 = 131548500301137262793340163377243958
    return decimal_value % fibonacci_180 == 0