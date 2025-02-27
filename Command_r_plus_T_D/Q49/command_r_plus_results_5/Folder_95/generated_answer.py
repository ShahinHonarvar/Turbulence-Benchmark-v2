def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_168 = 12586269025
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_168 == 0