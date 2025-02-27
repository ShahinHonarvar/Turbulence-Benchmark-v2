def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fibonacci_189 = 9954857822443614839
    return decimal_num % fibonacci_189 == 0