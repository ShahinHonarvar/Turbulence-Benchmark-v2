def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_164th = 18035502333207392863296
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_164th == 0