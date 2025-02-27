def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_126 = 12200160415121876738
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_126 == 0