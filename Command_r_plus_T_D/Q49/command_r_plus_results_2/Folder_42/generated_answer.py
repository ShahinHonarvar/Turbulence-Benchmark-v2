def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_146th = 6557470319842
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_146th == 0