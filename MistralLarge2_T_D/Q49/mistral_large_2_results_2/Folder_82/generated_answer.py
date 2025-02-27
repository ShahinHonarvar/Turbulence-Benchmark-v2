def if_decimal_is_divisible(binary_str):
    fib_99 = 218922995834555160530
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_99 == 0