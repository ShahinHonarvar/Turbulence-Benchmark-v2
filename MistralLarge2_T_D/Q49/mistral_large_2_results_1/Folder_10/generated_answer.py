def if_decimal_is_divisible(binary_str):
    fib_88 = 701408733
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_88 == 0