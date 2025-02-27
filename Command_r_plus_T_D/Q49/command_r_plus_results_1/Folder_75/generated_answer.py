def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_189th_num = 122001604151218463680000000
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_189th_num == 0