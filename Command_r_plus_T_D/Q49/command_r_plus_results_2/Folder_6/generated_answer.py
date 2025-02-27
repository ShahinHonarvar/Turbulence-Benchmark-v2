def if_decimal_is_divisible(binary_str):
    fib_185 = 1220016041512184636088006211643206830375
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_185 == 0