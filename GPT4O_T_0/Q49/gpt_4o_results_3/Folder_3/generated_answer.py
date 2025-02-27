def if_decimal_is_divisible(binary_str):
    fib_35 = 9227465
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_35 == 0