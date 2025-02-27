def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_78th_num = 927372692193078999176
    binary_int = int(binary_str, 2)
    return binary_int % fib_78th_num == 0