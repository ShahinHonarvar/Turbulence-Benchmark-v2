def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_90th_num = 218922995834555169089
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_90th_num == 0