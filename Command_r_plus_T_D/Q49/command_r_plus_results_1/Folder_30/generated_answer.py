def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_186th_num = 12586269025
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_186th_num == 0