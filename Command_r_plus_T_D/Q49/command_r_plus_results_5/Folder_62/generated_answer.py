def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_130th = 365435296162
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_130th == 0