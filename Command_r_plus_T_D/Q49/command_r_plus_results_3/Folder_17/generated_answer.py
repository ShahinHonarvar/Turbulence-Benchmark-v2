def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_154th_num = 267914296
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_154th_num == 0