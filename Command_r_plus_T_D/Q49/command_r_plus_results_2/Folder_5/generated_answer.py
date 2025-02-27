def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_85th = 1346269
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_85th == 0