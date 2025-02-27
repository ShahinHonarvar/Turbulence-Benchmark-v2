def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_135th_num = 836311903
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_135th_num == 0