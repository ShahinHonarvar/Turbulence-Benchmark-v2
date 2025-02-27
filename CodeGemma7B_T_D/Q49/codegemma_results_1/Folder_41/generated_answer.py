def if_decimal_is_divisible(bin_str):
    fib_67th = 134669529
    decimal = int(bin_str, 2)
    return decimal % fib_67th == 0