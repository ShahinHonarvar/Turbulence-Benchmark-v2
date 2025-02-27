def if_decimal_is_divisible(binary_str):
    fib_46 = 1836311903
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_46 == 0