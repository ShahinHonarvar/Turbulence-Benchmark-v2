def if_decimal_is_divisible(binary_str):
    fib_28 = 317811
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_28 == 0