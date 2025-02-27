def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_67th_number = 1907556567
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_67th_number == 0