def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_117th_num = 27777890035288
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_117th_num == 0