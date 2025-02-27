def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_114th_num = 2880067194370816120
    binary_int = int(binary_str, 2)
    return binary_int % fib_114th_num == 0