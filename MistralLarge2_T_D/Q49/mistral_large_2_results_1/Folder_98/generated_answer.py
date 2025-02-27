def if_decimal_is_divisible(binary_str):
    fib_14 = 377
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_14 == 0