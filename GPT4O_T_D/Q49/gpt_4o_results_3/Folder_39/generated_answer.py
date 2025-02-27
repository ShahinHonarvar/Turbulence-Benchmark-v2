def if_decimal_is_divisible(binary_str):
    fib15 = 377
    decimal_value = int(binary_str, 2)
    return decimal_value % fib15 == 0