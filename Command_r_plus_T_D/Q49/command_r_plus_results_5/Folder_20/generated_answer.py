def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_100th_num = 354224848179261915075
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_100th_num == 0