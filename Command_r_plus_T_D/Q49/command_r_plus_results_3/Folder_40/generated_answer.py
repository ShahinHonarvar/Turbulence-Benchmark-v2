def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_4th_num = 3
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_4th_num == 0