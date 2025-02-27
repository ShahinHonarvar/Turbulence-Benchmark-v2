def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib46 = 1836311903
    return decimal_num % fib46 == 0