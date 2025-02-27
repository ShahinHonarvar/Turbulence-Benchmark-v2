def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_170th = 1907556594862313321856001511702640830847111890847983559111776
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_170th == 0