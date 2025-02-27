def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_104 = 489835415466169411739280118862103953293048910
    return decimal_integer % fibonacci_104 == 0