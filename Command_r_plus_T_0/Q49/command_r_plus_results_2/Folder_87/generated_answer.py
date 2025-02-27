def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_180th = 12586269025
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_180th == 0