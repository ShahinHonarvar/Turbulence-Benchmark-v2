def if_decimal_is_divisible(binary_str):
    fib40 = 63245986
    decimal_value = int(binary_str, 2)
    return decimal_value % fib40 == 0