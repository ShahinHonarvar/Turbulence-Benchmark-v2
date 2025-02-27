def if_decimal_is_divisible(binary_str):
    fib_59 = 956722026041
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_59 == 0