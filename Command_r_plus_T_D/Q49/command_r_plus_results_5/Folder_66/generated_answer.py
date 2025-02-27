def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_120th_number = 36901539825264
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_120th_number == 0