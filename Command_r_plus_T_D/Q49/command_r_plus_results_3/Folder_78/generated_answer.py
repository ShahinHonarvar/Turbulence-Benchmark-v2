def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_115th_number = 19740274219868223167
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_115th_number == 0