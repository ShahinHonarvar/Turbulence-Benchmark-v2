def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_137th_num = 14472334024676221
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_137th_num == 0