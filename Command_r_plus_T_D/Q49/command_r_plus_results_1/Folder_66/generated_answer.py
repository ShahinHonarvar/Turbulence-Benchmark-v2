def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_120th = 12200160415121876738
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_120th == 0