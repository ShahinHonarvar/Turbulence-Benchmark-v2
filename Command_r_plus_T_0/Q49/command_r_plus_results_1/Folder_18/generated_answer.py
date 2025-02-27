def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_199th = 19880652004009201
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_199th == 0