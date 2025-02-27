def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_115th = 14472334024676221
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_115th == 0