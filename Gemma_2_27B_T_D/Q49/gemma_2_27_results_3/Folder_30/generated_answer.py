def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_186 = 1548008755920
    return decimal_value % fibonacci_186 == 0