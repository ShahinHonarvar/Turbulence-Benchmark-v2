def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_119th = 2971215073
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_119th == 0