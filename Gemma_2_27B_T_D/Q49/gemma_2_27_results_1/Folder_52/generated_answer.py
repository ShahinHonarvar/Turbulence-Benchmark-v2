def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_176 = 278026502984950338077406377290059513462
    return decimal_value % fibonacci_176 == 0