def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_88th_num = 308061521170129
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_88th_num == 0