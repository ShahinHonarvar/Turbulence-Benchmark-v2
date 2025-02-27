def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_174 = 14325481828340285959
    return decimal_value % fibonacci_174 == 0