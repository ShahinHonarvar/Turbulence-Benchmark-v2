def if_decimal_is_divisible(binary_str):
    fibonacci_num = 1066340417491710595814572169
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_num == 0