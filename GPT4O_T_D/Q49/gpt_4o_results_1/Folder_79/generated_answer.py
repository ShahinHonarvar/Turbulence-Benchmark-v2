def if_decimal_is_divisible(binary_str):
    fib_13th = 233
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_13th == 0