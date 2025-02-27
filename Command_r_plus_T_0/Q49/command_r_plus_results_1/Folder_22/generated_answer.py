def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_20th = 6765
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_20th == 0