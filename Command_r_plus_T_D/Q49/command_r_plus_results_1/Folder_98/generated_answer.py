def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_14th_num = 377
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_14th_num == 0