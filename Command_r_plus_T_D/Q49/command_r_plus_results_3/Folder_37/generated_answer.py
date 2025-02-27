def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_46th_num = 1836311903
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_46th_num == 0