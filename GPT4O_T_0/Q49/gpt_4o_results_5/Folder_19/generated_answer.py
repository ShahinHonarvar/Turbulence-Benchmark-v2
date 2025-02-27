def if_decimal_is_divisible(binary_str):
    fib_29 = 317811
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_29 == 0