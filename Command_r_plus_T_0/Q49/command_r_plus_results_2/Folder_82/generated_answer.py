def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_99th = 218922995834555169026
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_99th == 0