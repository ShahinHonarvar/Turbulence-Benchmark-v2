def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_185th_number = 122001604151218463680000000
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_185th_number == 0