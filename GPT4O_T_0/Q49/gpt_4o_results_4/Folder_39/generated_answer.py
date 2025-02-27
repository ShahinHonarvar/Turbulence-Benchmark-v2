def if_decimal_is_divisible(binary_str):
    fib_15th = 377
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_15th == 0