def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_125th = 8944394323791464
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_125th == 0