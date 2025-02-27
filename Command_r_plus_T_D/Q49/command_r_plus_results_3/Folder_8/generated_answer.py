def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_54th = 1836311903
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_54th == 0