def if_decimal_is_divisible(binary_str):
    fib_17th_num = 1597
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_17th_num == 0