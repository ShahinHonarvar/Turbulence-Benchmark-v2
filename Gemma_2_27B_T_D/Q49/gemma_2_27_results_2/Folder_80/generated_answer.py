def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_179 = 72574156153079997607974
    return decimal_value % fibonacci_179 == 0