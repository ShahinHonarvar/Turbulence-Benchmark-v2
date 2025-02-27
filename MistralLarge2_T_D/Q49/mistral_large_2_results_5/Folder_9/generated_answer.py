def if_decimal_is_divisible(binary_str):
    fib_68 = 72723460248141
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_68 == 0