def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_87th = 510303432486603638160117324173407
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_87th == 0