def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_45 = 701408733
    return decimal_value % fibonacci_45 == 0