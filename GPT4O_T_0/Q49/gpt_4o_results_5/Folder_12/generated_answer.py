def if_decimal_is_divisible(binary_str):
    fib_66 = 27777890035288
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_66 == 0