def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_168 = 1688055212249647314289191662948032916
    binary_int = int(binary_str, 2)
    return binary_int % fib_168 == 0