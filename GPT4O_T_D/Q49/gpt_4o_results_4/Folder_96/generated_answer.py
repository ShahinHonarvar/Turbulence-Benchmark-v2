def if_decimal_is_divisible(binary_str):
    fib_47 = 1836311903
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_47 == 0