def if_decimal_is_divisible(binary_str):
    fib_17 = 1597
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_17 == 0