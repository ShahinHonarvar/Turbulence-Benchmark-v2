def if_decimal_is_divisible(binary_str):
    fib46 = 1836311903
    decimal_value = int(binary_str, 2)
    return decimal_value % fib46 == 0