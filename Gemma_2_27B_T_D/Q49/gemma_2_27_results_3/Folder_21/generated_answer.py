def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fibonacci_195 = 165580141
    return decimal_num % fibonacci_195 == 0