def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_87th_num = 51030240522162809019539393600
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_87th_num == 0