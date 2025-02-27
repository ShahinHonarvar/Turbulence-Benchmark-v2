def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_110th_num = 319415926535897932382957812604929
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_110th_num == 0