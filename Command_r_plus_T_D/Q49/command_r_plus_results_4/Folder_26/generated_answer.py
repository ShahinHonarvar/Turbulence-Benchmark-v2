def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_138th_num = 1032041982484058368306310135407940124352784
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_138th_num == 0