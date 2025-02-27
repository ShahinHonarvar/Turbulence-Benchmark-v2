def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_180th_num = 1134903170
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_180th_num == 0