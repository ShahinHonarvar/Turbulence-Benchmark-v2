def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_134th = 1937488881376380804999158133401
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_134th == 0