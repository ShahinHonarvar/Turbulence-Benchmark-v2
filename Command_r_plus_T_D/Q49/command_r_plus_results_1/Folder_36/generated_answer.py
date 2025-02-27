def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_150th = 12586269025
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_150th == 0