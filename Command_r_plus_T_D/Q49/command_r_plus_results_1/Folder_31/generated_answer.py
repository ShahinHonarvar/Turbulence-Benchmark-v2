def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_69th_num = 102334155
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_69th_num == 0