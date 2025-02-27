def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_139th_num = 39603
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_139th_num == 0