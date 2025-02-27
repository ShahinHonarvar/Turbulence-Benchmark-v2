def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_38th = 39088169
    return decimal_num % fib_38th == 0