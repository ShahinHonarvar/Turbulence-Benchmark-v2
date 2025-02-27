def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fibonacci_47 = 2971215073
    return decimal_num % fibonacci_47 == 0