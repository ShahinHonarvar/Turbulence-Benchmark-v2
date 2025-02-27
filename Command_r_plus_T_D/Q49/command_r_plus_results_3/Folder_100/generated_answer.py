def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_190th = 2971215073
    binary_int = int(binary_str, 2)
    return binary_int % fib_190th == 0