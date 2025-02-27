def if_decimal_is_divisible(binary_str):
    fib_76 = 3416454622906707
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_76 == 0