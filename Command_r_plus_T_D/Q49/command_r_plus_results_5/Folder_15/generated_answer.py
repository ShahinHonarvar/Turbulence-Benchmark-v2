def if_decimal_is_divisible(binary_str):
    fib_9th_num = 21
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_9th_num == 0