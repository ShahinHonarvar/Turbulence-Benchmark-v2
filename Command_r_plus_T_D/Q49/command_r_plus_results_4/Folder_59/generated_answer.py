def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_74th_num = 24157817
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_74th_num == 0