def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_185th_number = 122001604151218
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_185th_number == 0