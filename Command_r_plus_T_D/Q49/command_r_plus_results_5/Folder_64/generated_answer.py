def if_decimal_is_divisible(binary_str):
    fib_10th_num = 55
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_10th_num == 0