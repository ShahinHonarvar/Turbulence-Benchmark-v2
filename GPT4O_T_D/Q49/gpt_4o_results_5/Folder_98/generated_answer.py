def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fib_14 = 377
    return decimal_value % fib_14 == 0