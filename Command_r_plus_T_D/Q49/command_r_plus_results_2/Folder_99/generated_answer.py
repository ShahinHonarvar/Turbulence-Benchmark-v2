def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_109th = 218922995834555169026
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_109th == 0