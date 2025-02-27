def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_87th_num = 514229
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_87th_num == 0