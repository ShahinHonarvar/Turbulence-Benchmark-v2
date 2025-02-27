def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_139th = 23416728348467685
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_139th == 0