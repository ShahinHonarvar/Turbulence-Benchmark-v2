def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_40th = 102334155
    return decimal_num % fib_40th == 0