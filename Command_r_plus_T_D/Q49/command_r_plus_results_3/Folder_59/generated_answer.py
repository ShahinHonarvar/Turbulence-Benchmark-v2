def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_74th_num = 130454329283030046651203864601210607
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_74th_num == 0