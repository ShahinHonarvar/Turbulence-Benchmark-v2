def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_137th = 25967968711186527440585
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_137th == 0