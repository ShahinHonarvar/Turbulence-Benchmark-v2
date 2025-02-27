def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_40th_num = 102334155
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_40th_num == 0